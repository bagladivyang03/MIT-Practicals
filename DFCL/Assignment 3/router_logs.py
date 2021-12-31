import pandas as pd

file = "logs.csv"

df = pd.read_csv(file)

dups = df.pivot_table(index = ['DIP'], aggfunc ='size')
df.drop_duplicates(subset ="DIP", keep = 'first', inplace = True)
result = pd.merge(df, dups.to_frame(), how="left", on="DIP")
result = result.rename(columns={0:"Count"})
print(result)

col_list = ["LIP","DIP","PN"]
file_pd = pd.read_csv(file, usecols = col_list)

def source(ip1, file_pd):
    selec = pd.DataFrame(file_pd.loc[file_pd["LIP"]==ip1])
    return selec

def des(ip1, file_pd):
    selec = pd.DataFrame(file_pd.loc[file_pd["DIP"]==ip1])
    return selec


def proto(ip1, file_pd):
    selec = pd.DataFrame(file_pd.loc[file_pd["PN"]==ip1])
    return selec

print("Select an Option:")
print("a) LIP")
print("b) DIP")
print("c) PN")
option =  str(input())
selec = file_pd

if option == "a":
    sip = str(input())
    selec = source(sip,selec)
    print(selec)
elif option == "b":
    dip = str(input())
    selec = des(dip,selec)
    print(selec)
elif option == "c":
    pip = str(input())
    selec = proto(pip,selec)
    print(selec)
else:
    print("Invalid option")


