thisglobal = "Rivaldo_Bogar = globalakses" # ini adalah variabel global dikarenakan variabel yang di deklarasikan sudah diluar  dari function


def myfunction(): # ini adalah function
    print("\nHello myname : " + thisglobal)


# pembuatan variabel pada lokal atau hanya bisa diakses di dalam function
def testinglokal(): # ini adalah function
    thislokal = "Rivaldo-Bogar = lokalakses"
    print("Hello myname : " + thislokal)
    print("Akses Global function : " + thisglobal)

def funcGlobalVar():
    global globalvar # gunanya global adalah untuk mendeklarasikan variabel global di dalam fucntion, sehingga bisa dia akses variabel lain
    globalvar = "Valdo_GameDeveloper" # assign value ke variabel
    print("global in function variabel = " + globalvar) # menampilkan 
    print("Akses Global function : " + thislokal) # tidak akan menampilkan lokal variabel,karena hanya diakses di lokal



myfunction() # pemanggilan function
testinglokal() #variabel lokal akses