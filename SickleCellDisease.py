
# Translating user input
def translate(var):
    
    ds = {"ATT":'I',"ATC":'I',"ATA":'I',
          "CTT":"L","CTC":"L","CTA":"L","CTG":"L","TTA":"L","TTG":"L",
          "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
          "TTT":"F","TTC":"F",
          "ATG":"M",}
    
    dkl = list(ds.keys())
    dvl =  list(ds.values())
    string = ""
    counter = 0
    new = []
    returnlist = ""
    returnlisthold = ""
    
    while counter != len(var):
        
        string = string + var[counter]
        
        if len(string) == 3:

            returnlisthold = returnlist
            
            for key in dkl:
                
                if string == key:
                    returnlist = returnlist + ds[string]
            string = ""

            if returnlisthold == returnlist:
                returnlist = returnlist + "X"
                
        counter = counter +1
    return returnlist 
        
var = raw_input("DNA: ").upper()
print translate(list(var))
print

# Translating DNAtxt and writing to mutatedDNA and normalDNA
def mutate():
    print_to_n = open('normalDNA.txt', 'w+')

    print_from = open('DNA.txt', 'r+')


    for line in print_from:
        line = line.upper()
        print_to_n.write(line)
        
    print_to_n.close()
    print_from.close()


    print_to_m = open('mutatedDNA.txt', 'w+')
    print_from = open('DNA.txt', 'r+')
    for line_m in print_from:
        line_m = line_m.replace("a", "T")
        print_to_m.write(line_m)

    print_to_m.close()
    print_from.close()


mutate()

# Translating normalDNA and mutatedDNA and displaying to user.
def txtTranslate():
    print_to_n = open('normalDNA.txt', 'r+')
    
    for line_nr in print_to_n:
                 
        translation1 = translate(line_nr)
        
        print translation1

       
    print_to_m = open('mutatedDNA.txt', 'r+')
    
    print "_______________________\n" # a line to differentiate between normal and mutated
    
    for line_mr in print_to_m:
                 
        translation2 = translate(line_mr)
        
        print translation2

                
txtTranslate()
    

