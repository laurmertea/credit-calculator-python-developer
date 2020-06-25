# to be tested as parameters for `credit_calc.py` and run in the CLI under the scripts directory

test_values = [
    "--type=diff --principal=1000000 --periods=10 --interest=10",
    "--type=annuity --principal=1000000 --periods=60 --interest=10",
    "--type=diff --principal=1000000 --payment=104000",
    "--type=diff --principal=500000 --periods=8 --interest=7.8",
    "--type=annuity --payment=8722 --periods=120 --interest=5.6",
    "--type=annuity --principal=500000 --payment=23000 --interest=7.8",
    "--type=annuity --principal=1000000 --periods=10 --payment=104000",
]
