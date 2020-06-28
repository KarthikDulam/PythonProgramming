import optimize as op

def main():
    budget = 800.0
    
    cards= [{"cardNickName": "Prime",
             "cardBalance": 1000,
             "cardApr": 18,
             "minPayment": 20,
             "maxPayment": 1000,
             "actualPayments": 200},
            {"cardNickName": "United",
             "cardBalance": 1800,
             "cardApr": 9,
             "minPayment": 36,
             "maxPayment": 1800,
             "actualPayments": 200},
             {"cardNickName": "B1",
             "cardBalance": 2000,
             "cardApr": 11,
             "minPayment": 25,
             "maxPayment": 2000,
             "actualPayments": 200},
             {"cardNickName": "B2",
             "cardBalance": 1300,
             "cardApr": 15,
             "minPayment": 40,
             "maxPayment": 1300,
             "actualPayments": 200}]


    model = op.Model(budget=budget,cards= cards)
    
    # Run the suggest payments routine for the above data
    sgst_pymnt = op.suggest_payments(model)
    print(sgst_pymnt)

    #Run the 12 Months Comparison routine
    tmonths = op.compare_12_months(model)
    print(tmonths)

if __name__ == "__main__":
    main()
