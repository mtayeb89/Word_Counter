def count_words(text):
    # Count the number of words in the text
    return len(text.split())

def count_characters(text):
    # Count the number of Characters in the text
    return len(text)

def count_lines(text):
    # Count the numbers of lines in the text
    return len(text.splitlines())

def analyze_file(filename):
    # Read a text file and analyze its content
    try:
        with open(filename,'r',encoding='utf-8')as file:
            content=file.read()
            word_count=count_words(content)
            char_count=count_characters(content)
            line_count=count_lines(content)

            print(f"Analyze results for file '{filename}':")
            print(f"Word count: {word_count}")
            print(f"Characters count: {char_count}")
    except FileNotFoundError:
        print(f"Error : File '{filename}' not found")
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
def show_help():
    # Display the help message
    print("Welcome to the word Counter app.")
    print("Usage:")
    print("1. To analyze a text file, type: analyze <filename>")
    print("2. To enter text directly, Type: text")
    print("3. To exit the program, type: exit")

def main():
    # the main function of the program
    show_help()
    while True:
        command=input("\n Enter Command: ").strip().split()
        if not command:
            continue
        if command[0]=="analyze" and len(command)==2:
            analyze_file(command[1])
        elif command[0]=="text":
            print("Enter the text (press Enter twice to finish)")
            text = ""
            while True:
                line=input()
                if line == "":
                    break
                text+=line+"\n"
                print(f"Word Count: {count_words(text)}")
                print(f"Character count: {count_characters(text)}")
                print(f"Line count: {count_lines(text)}")
        elif command[0]=="exit":
            print("Thank you for using word counter")
            break
        else:
            print("Invalid command. Please try again")
            show_help()
if __name__=="__main__":
    main()













