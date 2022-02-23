TEST_FILE = "human_hcd_tryp_best.msp"


import subprocess



def test(lang, test_name, test_input=TEST_FILE):
    print(" ======== Running " + test_name + "   ======== ")
    command = lang + " "  + test_name + " " + test_input
    subprocess.run("time " + command, shell=True, check=True)
    print("\n")


def main():
    test("python3", "py_readlines.py")
    test("bash", "cat.sh")
    test("bash", "dd.sh")
    test("perl", "perl_while.pl")

if __name__ == '__main__':
    main()
