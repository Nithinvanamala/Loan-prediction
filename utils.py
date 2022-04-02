import numpy as np 
import joblib 


def preprocessdata(Education, Self_Employed, ApplicantIncome,
        LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area):
    test_data = [[ Education, Self_Employed, ApplicantIncome,
        LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area] ]  
    trained_model = joblib.load("modelclf.pkl") 
    prediction = str(trained_model.predict(test_data))
   
    #return prediction 
    #prediction=prediction.item(0)
    #prediction=str(prediction)
    #return prediction[1]
    str1="You will not get loan because "
    if(prediction[1]=="0"):
        Credit_History=float(Credit_History)
        if(Credit_History<=0.42):
            str1+="Credit_History is low "
            LoanAmount =float(LoanAmount)
            if(LoanAmount<=132.5):
                str1+="and your income is not sufficient for loan approval"
            else:
                str1+="and your property area is not sufficient for loan approval"
        else:
            str1+="Loan amount is high"
        return str1
    else:
        return "Yes your loan will get approved"
 