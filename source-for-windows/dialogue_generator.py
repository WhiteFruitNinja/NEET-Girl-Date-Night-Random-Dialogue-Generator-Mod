#Made by WhiteFruitNinja

# Comment from WhiteFruitNinja
# My code is not good. Please don't judge again 😔.

import random
import os
import sys

unrpyc_code = ['#!/usr/bin/env python3\n', '\n', '# Copyright (c) 2012-2024 Yuri K. Schlesner, CensoredUsername, Jackmcbarn\n', '#\n', '# Permission is hereby granted, free of charge, to any person obtaining a copy\n', '# of this software and associated documentation files (the "Software"), to deal\n', '# in the Software without restriction, including without limitation the rights\n', '# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n', '# copies of the Software, and to permit persons to whom the Software is\n', '# furnished to do so, subject to the following conditions:\n', '#\n', '# The above copyright notice and this permission notice shall be included in\n', '# all copies or substantial portions of the Software.\n', '#\n', '# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n', '# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n', '# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n', '# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n', '# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n', '# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n', '# SOFTWARE.\n', '\n', '\n', '__title__ = "Unrpyc"\n', "__version__ = 'v2.0.2'\n", '__url__ = "https://github.com/CensoredUsername/unrpyc"\n', '\n', '\n', 'import argparse\n', 'import glob\n', 'import struct\n', 'import sys\n', 'import traceback\n', 'import zlib\n', 'from pathlib import Path\n', '\n', 'try:\n', '    from multiprocessing import Pool, cpu_count\n', 'except ImportError:\n', '    # Mock required support when multiprocessing is unavailable\n', '    def cpu_count():\n', '        return 1\n', '\n', 'import decompiler\n', 'import deobfuscate\n', 'from decompiler import astdump, translate\n', 'from decompiler.renpycompat import (pickle_safe_loads, pickle_safe_dumps, pickle_loads,\n', '                                    pickle_detect_python2)\n', '\n', '\n', 'class Context:\n', '    def __init__(self):\n', '        # list of log lines to print\n', '        self.log_contents = []\n', '\n', '        # any exception that occurred\n', '        self.error = None\n', '\n', '        # state of what case was encountered\n', '        # options:\n', '        #     error:      (default) an unexpected exception was raised\n', '        #     ok:         the process concluded successfully\n', '        #     bad_header: the given file cannot be parsed as a normal rpyc file\n', '        #     skip:       the given file was skipped due to a preexisting output file\n', '        self.state = "error"\n', '\n', '        # return value from the worker, if any\n', '        self.value = None\n', '\n', '    def log(self, message):\n', '        self.log_contents.append(message)\n', '\n', '    def set_error(self, error):\n', '        self.error = error\n', '\n', '    def set_result(self, value):\n', '        self.value = value\n', '\n', '    def set_state(self, state):\n', '        self.state = state\n', '\n', '\n', 'class BadRpycException(Exception):\n', '    """Exception raised when we couldn\'t parse the rpyc archive format"""\n', '    pass\n', '\n', '\n', '# API\n', '\n', 'def read_ast_from_file(in_file, context):\n', '    # Reads rpyc v1 or v2 file\n', '    # v1 files are just a zlib compressed pickle blob containing some data and the ast\n', '    # v2 files contain a basic archive structure that can be parsed to find the same blob\n', '    raw_contents = in_file.read()\n', '    file_start = raw_contents[:50]\n', '    is_rpyc_v1 = False\n', '\n', '    if not raw_contents.startswith(b"RENPY RPC2"):\n', "        # if the header isn't present, it should be a RPYC V1 file, which is just the blob\n", '        contents = raw_contents\n', '        is_rpyc_v1 = True\n', '\n', '    else:\n', '        # parse the archive structure\n', '        position = 10\n', '        chunks = {}\n', '        have_errored = False\n', '\n', '        for expected_slot in range(1, 0xFFFFFFFF):\n', '            slot, start, length = struct.unpack("III", raw_contents[position: position + 12])\n', '\n', '            if slot == 0:\n', '                break\n', '\n', '            if slot != expected_slot and not have_errored:\n', '                have_errored = True\n', '\n', '                context.log(\n', '                    "Warning: Encountered an unexpected slot structure. It is possible the \\n"\n', '                    "    file header structure has been changed.")\n', '\n', '            position += 12\n', '\n', '            chunks[slot] = raw_contents[start: start + length]\n', '\n', '        if 1 not in chunks:\n', "            context.set_state('bad_header')\n", '            raise BadRpycException(\n', '                "Unable to find the right slot to load from the rpyc file. The file header "\n', '                f"structure has been changed. File header: {file_start}")\n', '\n', '        contents = chunks[1]\n', '\n', '    try:\n', '        contents = zlib.decompress(contents)\n', '    except Exception:\n', "        context.set_state('bad_header')\n", '        raise BadRpycException(\n', '            "Did not find a zlib compressed blob where it was expected. Either the header has been "\n', '            f"modified or the file structure has been changed. File header: {file_start}") from None\n', '\n', "    # add some detection of ren'py 7 files\n", '    if is_rpyc_v1 or pickle_detect_python2(contents):\n', '        version = "6" if is_rpyc_v1 else "7"\n', '\n', '        context.log(\n', '            "Warning: analysis found signs that this .rpyc file was generated by ren\'py \\n"\n', "           f'    version {version} or below, while this unrpyc version targets ren\\'py \\n'\n", '            "    version 8. Decompilation will still be attempted, but errors or incorrect \\n"\n', '            "    decompilation might occur. ")\n', '\n', '    _, stmts = pickle_safe_loads(contents)\n', '    return stmts\n', '\n', '\n', 'def get_ast(in_file, try_harder, context):\n', '    """\n', '    Opens the rpyc file at path in_file to load the contained AST.\n', '    If try_harder is True, an attempt will be made to work around obfuscation techniques.\n', '    Else, it is loaded as a normal rpyc file.\n', '    """\n', "    with in_file.open('rb') as in_file:\n", '        if try_harder:\n', '            ast = deobfuscate.read_ast(in_file, context)\n', '        else:\n', '            ast = read_ast_from_file(in_file, context)\n', '    return ast\n', '\n', '\n', 'def decompile_rpyc(input_filename, context, overwrite=False, try_harder=False, dump=False,\n', '                   comparable=False, no_pyexpr=False, translator=None, init_offset=False,\n', '                   sl_custom_names=None):\n', '\n', '    # Output filename is input filename but with .rpy extension\n', '    if dump:\n', "        ext = '.txt'\n", "    elif input_filename.suffix == ('.rpyc'):\n", "        ext = '.rpy'\n", "    elif input_filename.suffix == ('.rpymc'):\n", "        ext = '.rpym'\n", '    out_filename = input_filename.with_suffix(ext)\n', '\n', '\n', '    if not overwrite and out_filename.exists():\n', "        context.log(f'Skipping {input_filename}. {out_filename.name} already exists.')\n", "        context.set_state('skip')\n", '        return\n', '\n', "    context.log(f'Decompiling {input_filename} to {out_filename.name} ...')\n", '    ast = get_ast(input_filename, try_harder, context)\n', '\n', "    with out_filename.open('w', encoding='utf-8') as out_file:\n", '        if dump:\n', '            astdump.pprint(out_file, ast, comparable=comparable, no_pyexpr=no_pyexpr)\n', '        else:\n', '            options = decompiler.Options(log=context.log_contents, translator=translator,\n', '                                         init_offset=init_offset, sl_custom_names=sl_custom_names)\n', '\n', '            decompiler.pprint(out_file, ast, options)\n', '\n', "    context.set_state('ok')\n", '\n', '\n', 'def worker_tl(arg_tup):\n', '    """\n', '    This file implements the first pass of the translation feature. It gathers TL-data from the\n', '    given rpyc files, to be used by the common worker to translate while decompiling.\n', '    arg_tup is (args, filename). Returns the gathered TL data in the context.\n', '    """\n', '    args, filename = arg_tup\n', '    context = Context()\n', '\n', '    try:\n', "        context.log(f'Extracting translations from {filename}...')\n", '        ast = get_ast(filename, args.try_harder, context)\n', '\n', '        tl_inst = translate.Translator(args.translate, True)\n', '        tl_inst.translate_dialogue(ast)\n', '\n', '        # this object has to be sent back to the main process, for which it needs to be pickled.\n', '        # the default pickler cannot pickle fake classes correctly, so manually handle that here.\n', '        context.set_result(pickle_safe_dumps((tl_inst.dialogue, tl_inst.strings)))\n', '        context.set_state("ok")\n', '\n', '    except Exception as e:\n', '        context.set_error(e)\n', "        context.log(f'Error while extracting translations from {filename}:')\n", '        context.log(traceback.format_exc())\n', '\n', '    return context\n', '\n', '\n', 'def worker_common(arg_tup):\n', '    """\n', '    The core of unrpyc. arg_tup is (args, filename). This worker will unpack the file at filename,\n', "    decompile it, and write the output to it's corresponding rpy file.\n", '    """\n', '\n', '    args, filename = arg_tup\n', '    context = Context()\n', '\n', '    if args.translator:\n', '        args.translator = pickle_loads(args.translator)\n', '\n', '    try:\n', '        decompile_rpyc(\n', '            filename, context, overwrite=args.clobber, try_harder=args.try_harder,\n', '            dump=args.dump, no_pyexpr=args.no_pyexpr, comparable=args.comparable,\n', '            init_offset=args.init_offset, sl_custom_names=args.sl_custom_names,\n', '            translator=args.translator)\n', '\n', '    except Exception as e:\n', '        context.set_error(e)\n', "        context.log(f'Error while decompiling {filename}:')\n", '        context.log(traceback.format_exc())\n', '\n', '    return context\n', '\n', '\n', 'def run_workers(worker, common_args, private_args, parallelism):\n', '    """\n', '    Runs worker in parallel using multiprocessing, with a max of `parallelism` processes.\n', '    Workers are called as worker((common_args, private_args[i])).\n', '    Workers should return an instance of `Context` as return value.\n', '    """\n', '\n', '    worker_args = ((common_args, x) for x in private_args)\n', '\n', '    results = []\n', '    if parallelism > 1:\n', '        with Pool(parallelism) as pool:\n', '            for result in pool.imap(worker, worker_args, 1):\n', '                results.append(result)\n', '\n', '                for line in result.log_contents:\n', '                    print(line)\n', '\n', '                print("")\n', '\n', '    else:\n', '        for result in map(worker, worker_args):\n', '            results.append(result)\n', '\n', '            for line in result.log_contents:\n', '                print(line)\n', '\n', '            print("")\n', '\n', '    return results\n', '\n', '\n', 'def parse_sl_custom_names(unparsed_arguments):\n', '    # parse a list of strings in the format\n', '    # classname=name-nchildren into {classname: (name, nchildren)}\n', '    parsed_arguments = {}\n', '    for argument in unparsed_arguments:\n', '        content = argument.split("=")\n', '        if len(content) != 2:\n', '            raise Exception(f\'Bad format in custom sl displayable registration: "{argument}"\')\n', '\n', '        classname, name = content\n', '        split = name.split("-")\n', '        if len(split) == 1:\n', '            amount = "many"\n', '\n', '        elif len(split) == 2:\n', '            name, amount = split\n', '            if amount == "0":\n', '                amount = 0\n', '            elif amount == "1":\n', '                amount = 1\n', '            elif amount == "many":\n', '                pass\n', '            else:\n', '                raise Exception(\n', '                    f\'Bad child node count in custom sl displayable registration: "{argument}"\')\n', '\n', '        else:\n', '            raise Exception(\n', '                f\'Bad format in custom sl displayable registration: "{argument}"\')\n', '\n', '        parsed_arguments[classname] = (name, amount)\n', '\n', '    return parsed_arguments\n', '\n', '\n', 'def plural_s(n, unit):\n', '    """Correctly uses the plural form of \'unit\' when \'n\' is not one"""\n', '    return f"1 {unit}" if n == 1 else f"{n} {unit}s"\n', '\n', '\n', 'def main():\n', '    if not sys.version_info[:2] >= (3, 9):\n', '        raise Exception(\n', '            f"\'{__title__} {__version__}\' must be executed with Python 3.9 or later.\\n"\n', '            f"You are running {sys.version}")\n', '\n', '    # argparse usage: python3 unrpyc.py [-c] [--try-harder] [-d] [-p] file [file ...]\n', '    cc_num = cpu_count()\n', '    ap = argparse.ArgumentParser(description="Decompile .rpyc/.rpymc files")\n', '\n', '    ap.add_argument(\n', "        'file',\n", '        type=str,\n', "        nargs='+',\n", '        help="The filenames to decompile. "\n', '        "All .rpyc files in any sub-/directories passed will also be decompiled.")\n', '\n', '    ap.add_argument(\n', "        '-c',\n", "        '--clobber',\n", "        dest='clobber',\n", "        action='store_true',\n", '        help="Overwrites output files if they already exist.")\n', '\n', '    ap.add_argument(\n', "        '--try-harder',\n", '        dest="try_harder",\n', '        action="store_true",\n', '        help="Tries some workarounds against common obfuscation methods. This is a lot slower.")\n', '\n', '    ap.add_argument(\n', "        '-p',\n", "        '--processes',\n", "        dest='processes',\n", "        action='store',\n", '        type=int,\n', '        choices=list(range(1, cc_num)),\n', '        default=cc_num - 1 if cc_num > 2 else 1,\n', '        help="Use the specified number or processes to decompile. "\n', '        "Defaults to the amount of hw threads available minus one, disabled when muliprocessing "\n', '        "unavailable is.")\n', '\n', "    astdump = ap.add_argument_group('astdump options', 'All unrpyc options related to ast-dumping.')\n", '    astdump.add_argument(\n', "        '-d',\n", "        '--dump',\n", "        dest='dump',\n", "        action='store_true',\n", '        help="Instead of decompiling, pretty print the ast to a file")\n', '\n', '    astdump.add_argument(\n', "        '--comparable',\n", "        dest='comparable',\n", "        action='store_true',\n", '        help="Only for dumping, remove several false differences when comparing dumps. "\n', '        "This suppresses attributes that are different even when the code is identical, such as "\n', '        "file modification times. ")\n', '\n', '    astdump.add_argument(\n', "        '--no-pyexpr',\n", "        dest='no_pyexpr',\n", "        action='store_true',\n", '        help="Only for dumping, disable special handling of PyExpr objects, instead printing them "\n', '        "as strings. This is useful when comparing dumps from different versions of Ren\'Py. It "\n', '        "should only be used if necessary, since it will cause loss of information such as line "\n', '        "numbers.")\n', '\n', '    ap.add_argument(\n', "        '--no-init-offset',\n", "        dest='init_offset',\n", "        action='store_false',\n", '        help="By default, unrpyc attempt to guess when init offset statements were used and insert "\n', '        "them. This is always safe to do for ren\'py 8, but as it is based on a heuristic it can be "\n', '        "disabled. The generated code is exactly equivalent, only slightly more cluttered.")\n', '\n', '    ap.add_argument(\n', "        '--register-sl-displayable',\n", '        dest="sl_custom_names",\n', '        type=str,\n', "        nargs='+',\n", '        help="Accepts mapping separated by \'=\', "\n', '        "where the first argument is the name of the user-defined displayable object, "\n', '        "and the second argument is a string containing the name of the displayable, "\n', '        "potentially followed by a \'-\', and the amount of children the displayable takes"\n', '        "(valid options are \'0\', \'1\' or \'many\', with \'many\' being the default)")\n', '\n', '    ap.add_argument(\n', "        '-t',\n", "        '--translate',\n", "        dest='translate',\n", '        type=str,\n', "        action='store',\n", '        help="Changes the dialogue language in the decompiled script files, using a translation "\n', '        "already present in the tl dir.")\n', '\n', '    ap.add_argument(\n', "        '--version',\n", "        action='version',\n", '        version=f"{__title__} {__version__}")\n', '\n', '    args = ap.parse_args()\n', '\n', "    # Catch impossible arg combinations so they don't produce strange errors or fail silently\n", '    if (args.no_pyexpr or args.comparable) and not args.dump:\n', '        ap.error("Options \'--comparable\' and \'--no_pyexpr\' require \'--dump\'.")\n', '\n', '    if args.dump and args.translate:\n', '        ap.error("Options \'--translate\' and \'--dump\' cannot be used together.")\n', '\n', '    if args.sl_custom_names is not None:\n', '        try:\n', '            args.sl_custom_names = parse_sl_custom_names(args.sl_custom_names)\n', '        except Exception as e:\n', '            print("\\n".join(e.args))\n', '            return\n', '\n', '    def glob_or_complain(inpath):\n', '        """Expands wildcards and casts output to pathlike state."""\n', '        retval = [Path(elem).resolve(strict=True) for elem in glob.glob(inpath, recursive=True)]\n', '        if not retval:\n', "            print(f'Input path not found: {inpath}')\n", '        return retval\n', '\n', '    def traverse(inpath):\n', '        """\n', '        Filters from input path for rpyc/rpymc files and returns them. Recurses into all given\n', '        directories by calling itself.\n', '        """\n', "        if inpath.is_file() and inpath.suffix in ['.rpyc', '.rpymc']:\n", '            yield inpath\n', '        elif inpath.is_dir():\n', '            for item in inpath.iterdir():\n', '                yield from traverse(item)\n', '\n', '    # Check paths from argparse through globing and pathlib. Constructs a tasklist with all\n', "    # `Ren'Py compiled files` the app was assigned to process.\n", '    worklist = []\n', '    for entry in args.file:\n', '        for globitem in glob_or_complain(entry):\n', '            for elem in traverse(globitem):\n', '                worklist.append(elem)\n', '\n', "    # Check if we actually have files. Don't worry about no parameters passed,\n", '    # since ArgumentParser catches that\n', '    if not worklist:\n', '        print("Found no script files to decompile.")\n', '        return\n', '\n', '    if args.processes > len(worklist):\n', '        args.processes = len(worklist)\n', '\n', '    print(f"Found {plural_s(len(worklist), \'file\')} to process. "\n', '          f"Performing decompilation using {plural_s(args.processes, \'worker\')}.")\n', '\n', '    # If a big file starts near the end, there could be a long time with only one thread running,\n', '    # which is inefficient. Avoid this by starting big files first.\n', '    worklist.sort(key=lambda x: x.stat().st_size, reverse=True)\n', '\n', '    translation_errors = 0\n', '    args.translator = None\n', '    if args.translate:\n', '        # For translation, we first need to analyse all files for translation data.\n', '        # We then collect all of these back into the main process, and build a\n', '        # datastructure of all of them. This datastructure is then passed to\n', '        # all decompiling processes.\n', '        # Note: because this data contains some FakeClasses, Multiprocessing cannot\n', '        # pass it between processes (it pickles them, and pickle will complain about\n', '        # these). Therefore, we need to manually pickle and unpickle it.\n', '\n', '        print("Step 1: analysing files for translations.")\n', '        results = run_workers(worker_tl, args, worklist, args.processes)\n', '\n', "        print('Compiling extracted translations.')\n", '        tl_dialogue = {}\n', '        tl_strings = {}\n', '        for entry in results:\n', '            if entry.state != "ok":\n', '                translation_errors += 1\n', '\n', '            if entry.value:\n', '                new_dialogue, new_strings = pickle_loads(entry.value)\n', '                tl_dialogue.update(new_dialogue)\n', '                tl_strings.update(new_strings)\n', '\n', '        translator = translate.Translator(None)\n', '        translator.dialogue = tl_dialogue\n', '        translator.strings = tl_strings\n', '        args.translator = pickle_safe_dumps(translator)\n', '\n', '        print("Step 2: decompiling.")\n', '\n', '    results = run_workers(worker_common, args, worklist, args.processes)\n', '\n', '    success = sum(result.state == "ok" for result in results)\n', '    skipped = sum(result.state == "skip" for result in results)\n', '    failed = sum(result.state == "error" for result in results)\n', '    broken = sum(result.state == "bad_header" for result in results)\n', '\n', '    print("")\n', '    print(f"{55 * \'-\'}")\n', '    print(f"{__title__} {__version__} results summary:")\n', '    print(f"{55 * \'-\'}")\n', '    print(f"Processed {plural_s(len(results), \'file\')}.")\n', '\n', '    print(f"> {plural_s(success, \'file\')} were successfully decompiled.")\n', '\n', '    if broken:\n', '        print(f"> {plural_s(broken, \'file\')} did not have the correct header, "\n', '              "these were ignored.")\n', '\n', '    if failed:\n', '        print(f"> {plural_s(failed, \'file\')} failed to decompile due to errors.")\n', '\n', '    if skipped:\n', '        print(f"> {plural_s(skipped, \'file\')} were skipped as the output file already existed.")\n', '\n', '    if translation_errors:\n', '        print(f"> {plural_s(translation_errors, \'file\')} failed translation extraction.")\n', '\n', '\n', '    if skipped:\n', '        print("")\n', '        print("To overwrite existing files instead of skipping them, use the --clobber flag.")\n', '\n', '    if broken:\n', '        print("")\n', '        print("To attempt to bypass modifications to the file header, use the --try-harder flag.")\n', '\n', '    if failed:\n', '        print("")\n', '        print("Errors were encountered during decompilation. Check the log for more information.")\n', '        print("When making a bug report, please include this entire log.")\n', '\n', "if __name__ == '__main__':\n", '    main()\n']

words = list()
ignore_files = list()
symbols_and_words = list()

ignore_files = ['screens.rpy', 'options.rpy', 'gui.rpy', 'custom_styles.rpy', 'custom.rpy']
allowed_symbols_and_words = ['"']
prohibited_symbols_and_words = ['(', ')', '==', '[', ']', '#', 'play sound', 'play music', 'play audio', 'show text', 'play bg']

def check_if_unrenpyc_file_exist():
    if os.path.exists('game/unrpyc.py'):
        print("the file exist")
    elif not os.path.isdir('game/unrpyc.py'):
        print("the file doesn't exist")
        with open("game/unrpyc.py", "w") as wf:
            wf.writelines(unrpyc_code)


def read_txt_file():
    global words
    with open("english_word_list.txt", "r") as f:
        for line in f:
            line_words = line.strip().split()
            words.extend(line_words)

def create_sentence(length_of_sentence, words):
    sentence = '"' + ' '.join(random.choices(words, k=length_of_sentence)).capitalize() + "." + '"'

    return sentence

def write_sentence_in_rpy_files(text_list):
    filtered_text_list = list()
    
    for text in text_list:

        # Check if any allowed symbol is in the text
        has_allowed = any(symbol in text for symbol in allowed_symbols_and_words)
        # Check if none of the prohibited symbols are in the text
        has_prohibited = any(symbol in text for symbol in prohibited_symbols_and_words)

        if has_allowed and not has_prohibited:

            initial_spaces = True
            spaces = 0
            is_character_name_not_full = True
            character_name = str()
            inside_quote = False
            colon = str()

            length_of_sentence = random.randint(1, 20)
            generated_sentence = create_sentence(length_of_sentence, words)

            # Every text's symbol loop
            for symbol in text:

                if symbol == '"' and not inside_quote:
                    inside_quote = True
                elif symbol == '"' and inside_quote:
                    inside_quote = False

                if symbol == " " and initial_spaces:
                    spaces += 1
                elif not symbol == " " and not symbol == '"' and is_character_name_not_full:
                    initial_spaces = False
                    character_name += symbol
                elif symbol == ":" and not inside_quote:
                    colon = symbol
                else:
                    initial_spaces = False
                    is_character_name_not_full = False
                    continue

            if character_name == "":
                filtered_text_list.append(f'{spaces * " "}{character_name}{generated_sentence}{colon}\n')
            else:
                filtered_text_list.append(f'{spaces * " "}{character_name} {generated_sentence}{colon}\n')
        else:
            filtered_text_list.append(text)

    return filtered_text_list

def check_if_copy_of_original_rpy_files_exist():
    text_list = list()
    folder_exist = bool()

    folder_exist = False

    if os.path.isdir('copy_of_original_rpy_files') and os.path.isdir('game'):
        print("the folder exist")
        folder_exist = True
    elif not os.path.isdir('copy_of_original_rpy_files') and os.path.isdir('game'):
        print("the folder doesn't exist")
        folder_exist = False
        os.mkdir('copy_of_original_rpy_files')

    return folder_exist

def read_and_write_rpy_files():
    text_list = list()

    # Get the directory of the current script
    if getattr(sys, 'frozen', False):  # Check if the application is frozen
        # The application is run as a bundle
        script_dir = os.path.dirname(sys.executable)
    else:
        # The application is run as a script
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    copy_rpy_files_dir = os.path.join(script_dir + "/copy_of_original_rpy_files")

    folder_exist = check_if_copy_of_original_rpy_files_exist()

    for root, dirs, files in os.walk(script_dir + "/game"):
        for file in files:
            if file in ignore_files or not file.endswith('.rpy'):
                continue
            
            if file.endswith('.rpy'):
                # Reads file
                if not folder_exist:
                    with open(os.path.join(root, file), 'r') as f:
                        text_list.extend(f.readlines())
                    
                    with open(os.path.join(copy_rpy_files_dir, file), 'w') as wf:
                        wf.writelines(text_list)

                    with open(os.path.join(root, file), 'w') as wf:
                        wf.writelines(write_sentence_in_rpy_files(text_list))
                
                if folder_exist:
                    with open(os.path.join(copy_rpy_files_dir, file), 'r') as f:
                        text_list.extend(f.readlines())
                
                    with open(os.path.join(root, file), 'w') as wf:
                        wf.writelines(write_sentence_in_rpy_files(text_list))

                text_list.clear()
                
    words.clear()
    return text_list

def revert_original_rpy_files():
    text_list = list()

    if getattr(sys, 'frozen', False):  # Check if the application is frozen
        # The application is run as a bundle
        script_dir = os.path.dirname(sys.executable)
    else:
        # The application is run as a script
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    copy_rpy_files_dir = os.path.join(script_dir + "/copy_of_original_rpy_files")

    for root, dirs, files in os.walk(script_dir + "/game"):
        for file in files:
            if file in ignore_files or not file.endswith('.rpy'):
                continue
            
            if file.endswith('.rpy'):
                with open(os.path.join(copy_rpy_files_dir, file), 'r') as f:
                    text_list.extend(f.readlines())
                
                with open(os.path.join(root, file), 'w') as wf:
                    wf.writelines(text_list)

                text_list.clear()
                
    words.clear()
    return text_list
