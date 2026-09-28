def get_user_input():
     file_path=input("input your file: ")
     search_symbol=(input("input your symbol:"))
     return(file_path, search_symbol)

def counter(file_path, search_symbol):
    with open(file_path, "r", encoding="utf-8") as shader_file:
        symbol_counter= 0
        for line in  shader_file:
                position=line.find(search_symbol)
                if position != -1:
                #print(letter[:5])
                    print(line)
            # if position != -1:
                    symbol_counter=symbol_counter+1            
    print(symbol_counter)

def main():
     file_path, search_symbol= get_user_input()
     counter(file_path, search_symbol)
if __name__=="__main__":
    main()    