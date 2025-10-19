"""
---
(c) 2025 David SPORN
---
This is part of 'The python library for the isa68k-database project, by Sporniket'.

'The python library for the isa68k-database project, by Sporniket' is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

'The python library for the isa68k-database project, by Sporniket' is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with 'The python library for the isa68k-database project, by Sporniket'.
If not, see <https://www.gnu.org/licenses/>. 
---
"""
import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

def createArgParser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="python3 -m isa68k_db_lib_by_sporniket.db2html",
        description="Pretty prints a source file written in assembly language.",
        epilog="""---
(c) 2024 David SPORN
---
This is part of 'The python library for the isa68k-database project, by Sporniket'.

'The python library for the isa68k-database project, by Sporniket' is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

'The python library for the isa68k-database project, by Sporniket' is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with SPASM.
If not, see <https://www.gnu.org/licenses/>. 
---
""",
        formatter_class=RawDescriptionHelpFormatter,
        allow_abbrev=False,
    )

    # Add the arguments
    parser.add_argument(
        "--output",
        metavar="<output file>",
        type=str,
        help="When given, will save the result into the specified file instead of the standard output",
    )

    parser.add_argument(
        "sources",
        metavar="<source files...>",
        type=str,
        nargs="*",
        help="a list of source files",
    )

    commandGroup = parser.add_mutually_exclusive_group(required=False)
    commandGroup.add_argument(
        "-r",
        "--rewrite",
        action="store_true",
        help=f"Replace the source files by their pretty-printed version WHEN THERE IS A DIFFERENCE.",
    )

    return parser


def processDatabase(db:list[str]) -> list[str]:
    DB_MAPPING = [
        ["metadata","row_id"],
        ["metadata","mnemonic"],
        ["metadata","synopsys"],
        ["metadata","opcode"],
        ["metadata","supplemental_word_1"],
        ["metadata","supplemental_word_2"],
        ["metadata","domain"],
        ["metadata","size_b"],
        ["metadata","size_w"],
        ["metadata","size_l"],
        ["metadata","number_of_operands"],
        #
        ["operand1","is_recipient"],
        ["operand1","data_reg_direct"],
        ["operand1","addr_reg_direct"],
        ["operand1","addr_reg_indirect"],
        ["operand1","addr_reg_indirect_postinc"],
        ["operand1","addr_reg_indirect_predec"],
        ["operand1","addr_reg_indirect_displace"],
        ["operand1","addr_reg_indirect_displace_index"],
        ["operand1","addr_reg_indirect_base_displace_index"],
        ["operand1","memory_indirect_postindex"],
        ["operand1","memory_indirect_preindex"],
        ["operand1","pc_indirect_displace"],
        ["operand1","pc_indirect_displace_index"],
        ["operand1","pc_indirect_base_displace_index"],
        ["operand1","pc_memory_indirect_postindex"],
        ["operand1","pc_memory_indirect_preindex"],
        ["operand1","abs_short"],
        ["operand1","abs_long"],
        ["operand1","immediate"],
        ["operand1","signed_value"],
        #
        ["operand2","is_recipient"],
        ["operand2","data_reg_direct"],
        ["operand2","addr_reg_direct"],
        ["operand2","addr_reg_indirect"],
        ["operand2","addr_reg_indirect_postinc"],
        ["operand2","addr_reg_indirect_predec"],
        ["operand2","addr_reg_indirect_displace"],
        ["operand2","addr_reg_indirect_displace_index"],
        ["operand2","addr_reg_indirect_base_displace_index"],
        ["operand2","memory_indirect_postindex"],
        ["operand2","memory_indirect_preindex"],
        ["operand2","pc_indirect_displace"],
        ["operand2","pc_indirect_displace_index"],
        ["operand2","pc_indirect_base_displace_index"],
        ["operand2","pc_memory_indirect_postindex"],
        ["operand2","pc_memory_indirect_preindex"],
        ["operand2","abs_short"],
        ["operand2","abs_long"],
        ["operand2","immediate"],
        ["operand2","signed_value"],
        #
        ["operand3","is_recipient"],
        ["operand3","data_reg_direct"],
        ["operand3","addr_reg_direct"],
        ["operand3","addr_reg_indirect"],
        ["operand3","addr_reg_indirect_postinc"],
        ["operand3","addr_reg_indirect_predec"],
        ["operand3","addr_reg_indirect_displace"],
        ["operand3","addr_reg_indirect_displace_index"],
        ["operand3","addr_reg_indirect_base_displace_index"],
        ["operand3","memory_indirect_postindex"],
        ["operand3","memory_indirect_preindex"],
        ["operand3","pc_indirect_displace"],
        ["operand3","pc_indirect_displace_index"],
        ["operand3","pc_indirect_base_displace_index"],
        ["operand3","pc_memory_indirect_postindex"],
        ["operand3","pc_memory_indirect_preindex"],
        ["operand3","abs_short"],
        ["operand3","abs_long"],
        ["operand3","immediate"],
        #
        ["metadata","brief"],
        #
        ["scope","020_or_later"],
        ["scope","020_only"],
        ["scope","000_excluded"],
        ["scope","040_excluded"],
        ["scope","000_008_only"],
        ["scope","040_only"],
    ]
    mappedDb = []
    result=[]
    for dbRec in db:
        dbRecSplitted = dbRec.split("\t")
        intermediateRepresentation ={"metadata":{}, "operand1":{}, "operand2":{}, "operand3":{}, "scope":{}}
        for colindex,mapping in enumerate(DB_MAPPING):
            intermediateRepresentation[mapping[0]][mapping[1]] = dbRecSplitted[colindex]
        mappedDb += [intermediateRepresentation]
        # process on the go
        result += [
            "<h3>"+intermediateRepresentation["metadata"]["synopsys"]+"</h3>",
            "<p>"+intermediateRepresentation["metadata"]["brief"]+"</p>",
        ]


    return result

def postprocessResult(source:list[str]) -> list[str]:
    return ["<html>","<head>","<title>isa68k_db_lib_by_sporniket.db2html</title>","</head>","<body>"]+source+["</body>","</html>"]

def main():
    try:
        args = createArgParser().parse_args()
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1
    else:
        if len(args.sources) > 0:
            # EITHER process given list of files...
            sourcesErrors = []

            # -- Check the list of files
            for source in args.sources:
                if os.path.exists(source):
                    if os.path.isfile(source):
                        # NO PROBLEM
                        continue
                    else:
                        sourcesErrors += [
                            {"errorType": "NOT_A_FILE", "path": source}
                        ]
                else:
                    sourcesErrors += [{"errorType": "MISSING_FILE", "path": source}]
            if len(sourcesErrors) > 0:
                report = []
                for e in sourcesErrors:
                    message = (
                        f"* MISSING : {e['path']}"
                        if e["errorType"] == "MISSING_FILE"
                        else f"* NOT A FILE : {e['path']}"
                    )
                    report += [message]
                report = "\n".join(report)
                print(
                    f"ERROR -- in given list of files :\n{report}", file=sys.stderr
                )
                return 1

            # -- Proceed
            result = []
            for source in args.sources:
                with open(source, "rt") as f:
                    lines = f.readlines()
                    result += processDatabase(lines)
            result = postprocessResult(result)
            if args.output:
                # Save to file
                with open(args.output, "wt") as f:
                    f.write("\n".join(result))
                    f.write("\n")
            else:
                # Normal mode
                print("\n".join(result))
                print("\n")
        else:
            # ...OR process standard input

            # -- Proceed
            result = []
            for line in sys.stdin:
                result += processDatabase([line])
            result = postprocessResult(result)
            print("\n".join(result))
            print("\n")


        return 0    


if __name__ == "__main__":
    main()
