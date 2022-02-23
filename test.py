TEST_FILES = ["human_hcd_tryp_best.msp", "LICENSE"]


import subprocess



def test(lang, test_name, test_input):
    print(" ======== Running " + test_name + "   ======== ")
    command = lang + " "  + test_name + " " + test_input
    subprocess.run("time " + command, shell=True, check=True)
    print("\n")


def main():
    for fin in TEST_FILES:
        print(" TESTING " , fin)
        test("python3", "py_readlines.py", fin)
        test("bash", "cat.sh", fin)
        test("bash", "dd.sh", fin)
        test("perl", "perl_while.pl", fin)

if __name__ == '__main__':
    main()
