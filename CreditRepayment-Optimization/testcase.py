import optimze as op

def main():
    budget = 100.0
    cards= [{"cardNickName": "Prime",
             "cardBalance": 1000,
             "cardApr": 15,
             "minPayment": 20,
             "maxPayment": 1000,
             "actualPayments": 50},
            {"cardNickName": "United",
             "cardBalance": 1800,
             "cardApr": 18,
             "minPayment": 36,
             "maxPayment": 1800,
             "actualPayments": 50}]

    model = op.Model(budget=budget,cards= cards)
    
    # Run the suggest payments routine for the above data
    sgst_pymnt = op.suggest_payments(model)
    print(sgst_pymnt)

    #Run the 12 Months Comparison routine
    tmonths = op.compare_12_months(model)
    print(tmonths)

if __name__ == "__main__":
    main()
