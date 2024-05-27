import netfilterqueue,  optparse
import scapy.all as scapy


def search_file():
    keyword=options.search.lower()
    line_count=0
    if options.case:
        keyword=options.search

    keyword_count = 0
    with open(options.file,'r') as file:
        for line in file:
            if not options.case:
                line=line.lower()
            line_count += 1
            if keyword in line:
                keyword_count += 1
                print(f"[+] keyword [ {options.search} ] in line {line_count}")
    print(f"[+] {keyword_count} times found")


def search_text():
    state = None
    keyword=options.search.lower()
    text=options.text.lower()
    if options.case:
        keyword=options.search
        text=options.text

    if  keyword in text:
        keyword_count = options.text.lower().count(options.search.lower())
        print(f"[+] keyword  [ {options.search} ] {keyword_count} times found")
        state = 1
    if state is None:
        print("[+] no keyword found")
            

def arguemnts():
    parser = optparse.OptionParser()
    parser.add_option("-k","--keyword",dest="search",help="Search word")
    parser.add_option("-f","--file",dest="file",help="File path")
    parser.add_option("-t","--text",dest="text",help="input text")
    parser.add_option("-c","--CaseSenstive",action="store_true",dest="case",help="CaseSenstive")
    options,arguemnts = parser.parse_args()

    return options

options = arguemnts()
if  options.search is None:
    print("[log] -h for help")
if options.file:
    search_file()
else:
    search_text()


