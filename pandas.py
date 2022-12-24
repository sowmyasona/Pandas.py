# pandas are used for creating dataframes
import pandas
d=pandas.read_csv("D:\Programming\Python.py\Errorhandling")
print(d)


# import pandas as pd
# df=pd.read_excel("D:\Python Programs\Day_32\Pandas\B100.xlsx")
# print(df)

# we creating a dataframe with the help of dictionaries
# sjosh={"sid":[1,2,3,4],
#        "sname":["Naveen","Sai","Praveen","azeez"],
#        "scourse":["C","Full Stack","Python","Advance Python"],
#        "sdoj":["Nov","May","July","Sept"]
#        }
# print(sjosh,type(sjosh))
# import pandas as pd
# df2=pd.DataFrame(sjosh)
# print(df2)

# we now create a dataframe with the help of tuples
# import pandas as pd
# empdata=[(101,"karthik",),(202,"Sneha","Vij"),(305,"priya","Himachal"),(401,"Karthik","Kurnool")]
# df3=pd.DataFrame(empdata,columns=["sid","sname","splace"])
# print(df3)