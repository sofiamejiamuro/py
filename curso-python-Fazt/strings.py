myStr = "Hello World"

# dir() enseña que tipo de métodos se pueden hacer con un dato

dir(myStr)
#print(dir(myStr))

print(myStr.upper()) # HELLO WORLD

print(myStr.lower()) # hello world 

print(myStr.swapcase()) # hELLO wORLD

print(myStr.capitalize()) # Hello world

print(myStr.replace("Hello", "Hola")) #Hola World 

print(myStr.count('l')) # 3
print(myStr.count(' ')) # 1 

print(myStr.startswith('hello')) # False
print(myStr.startswith('Hello')) # True
print(myStr.startswith('H')) # True


print(myStr.endswith('world')) # False
print(myStr.endswith('World')) # True
 
print(myStr.split()) # ['Hello', 'World'] --> una lista

print(myStr.split('o')) # ['Hell', ' W', 'rld'] --> una lista

print(myStr.find('o')) #4 --> posicion
print(myStr.find('H')) #0

print(len(myStr)) #11

print(myStr.index('H')) # 0

print(myStr.isnumeric()) # False

print(myStr.isalpha()) # False

print(myStr[4]) # o
print(myStr[-1]) # d

print(myStr + " from Python") # Hello World from Python
print(f"{myStr} from Python") # Hello World from Python

# Métodos encadenados
print(myStr.replace("Hello", "Hola").upper())

