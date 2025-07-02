import nltk
import re
from nltk import PorterStemmer
s=PorterStemmer()

# Read Carefully

# Rules to Run the program:

# Unfortunately gold query data set has some minor issues in results
# Do not change the directory as it will cause problems
# After unzipping the folder first install nltk library
# Command for installation: pip install nltk
# Then run this file
# This file will make some warnings regarding txt files  (Ignore them)
# It will take some time to run as there are 448 files
# Some time it will take more time, (do not assume that program has crashed), it just need time to process
# Original files are in the folder named (Text_files)
# Updated Tokenized files will be created in the folder named (Updated_text_files)
# First Write the query for AND/OR/NOT when program asks about
# You will get the result set
# Then Write the query for w1 w2 /n when program asks about
# You will get the result set 



stop_words=[
    "a","is","the","of","all","and","to","can","be",
    "as","once","for","at","am","are","has","have","had",
    "up", "his","her","in","on","no","we","do"]

size=448
inv_index={}
pos_index={}


# Function to remove stop words and punctuaion marks

def filter_words():
    # size=448
    for temp in range(1,size+1):
        u_all_line=[]
        with open(f"Text_files\{temp}.txt","r") as file:
            all_lines=file.readlines()

            for s_line in all_lines:
                s_line=s_line.casefold()
                s_line=re.sub(r"[^a-zA-Z\s]", " ", s_line)
                filter_w=[]
                words=s_line.split()
                for word in words:
                    if word not in stop_words:
                        filter_w.append(word)

                update_line = " ".join(filter_w)
                u_all_line.append(update_line + "\n")
        file.close()

        with open(f"Updated_text_files\{temp}.txt","w") as file:
            file.writelines(u_all_line)
        file.close()
    
    print("\n\n\t\t******** Welcome to Boolean Retrieval Model ********")
    print("\n\t\t** Tokenization Of Documents has been Completed **\n")
    return


# Function for stemming words using PorterStemmer

def token_stem():
    stem_w=[]
    update_line=[]
    # size=448
    for i in range(1,size+1):
        update_line.clear()
        with open(f"Updated_text_files\{i}.txt","r") as file:
            my_list=file.readlines()
            for line in my_list:
                words=line.split()
                stem_w.clear()
                for s_word in words:
                    str1=s.stem(s_word)
                    stem_w.append(str1)
                update_line.append(" ".join(stem_w) + "\n")
        file.close()

        with open(f"Updated_text_files\{i}.txt","w") as file:
            file.writelines(update_line)
        file.close()
    return


# Function to created Inverted Index Dictionary

def inv_index_func():
    # size=448
    for i in range(1,size+1):
        d_name=f"{i}"
        with open(f"Updated_text_files\{i}.txt","r") as file:
            for s_line in file:
                all_words=s_line.split()
                for s_word in all_words:
                    if s_word in inv_index:
                        if d_name not in inv_index[s_word]:
                            inv_index[s_word].append(d_name)
                    else:
                        inv_index[s_word]=[d_name]
        file.close()
    print("Inverted Index Dictionary Created Succesfully")
    return


# Function to create Positional Index Dictionary

def pos_index_func():
    # size=448
    for i in range(1,size+1):
        d_name=f"{i}"
        with open(f"Updated_text_files\{i}.txt", "r") as file:
            pos=0
            for s_line in file:
                all_words=s_line.split()
                for s_word in all_words:
                    pos+=1
                    if s_word in pos_index:
                        pos_index[s_word].append((d_name,pos))
                    else:
                        pos_index[s_word]=[(d_name,pos)]
        file.close()

    print("Positional Index Dictionary Created Sucessfully")
    return



# Function to process AND/OR/NOT QUeries and, retireve the matched Docs (For Inverted Index Queries)

def inv_query():
    print("\n\t\t**** Enter Boolean Query Having AND, OR, NOT ****")
    opt=input().strip()
    words=opt.split()
    p_words=[]
    operators=[]
    for s_word in words:
        if s_word.upper() in ["AND","OR","NOT"]:
            operators.append(s_word.upper())
        else:
            s_word=s_word.casefold()
            s_word=re.sub(r"[^a-zA-Z\s]", "",s_word)
            s_word=s.stem(s_word)  
            p_words.append(s_word)

    print(f"Processed Query: {p_words}")
    doc_sets=[]
    for s_word in p_words:
        if s_word in inv_index:
            doc_sets.append(set(inv_index[s_word]))
        else:
            doc_sets.append(set())
    if len(doc_sets)==0:
        return set()

    ans=doc_sets[0]
    i=0
    while i<len(operators):
        op=operators[i]
        if op=="AND":
            ans=ans & doc_sets[i+1]
        elif op=="OR":
            ans=ans | doc_sets[i+1]
        elif op=="NOT":
            ans=ans - doc_sets[i+1]
        i+=1 
    return ans



# Function to process and then retrive the matched documents  (For Positional Index Querirs)  

def pos_query():
    print("\n\t\t**** Enter Positional Query in format: word1 word2 /N ****")
    opt=input().strip()
    ex_word=re.match(r"(\w+)\s+(\w+)\s*/(\d+)",opt)
    if not ex_word:
        print("Invalid Input, Crashing Positional Index")
        return set()

    w1,w2,dist=ex_word.groups()
    dist=int(dist)
    s_w1=w1.casefold()
    s_w1=re.sub(r"[^a-zA-Z\s]", "",s_w1)
    s_w1=s.stem(s_w1)
    s_w2=w2.casefold()
    s_w2=re.sub(r"[^a-zA-Z\s]", "",s_w2)
    s_w2=s.stem(s_w2)

    print(f"Processed Query: {s_w1} {s_w2} / {dist} ")

    if s_w1 not in pos_index or s_w2 not in pos_index:
        return set()
    doc_1=set()
    for doc, _ in pos_index[s_w1]:
        doc_1.add(doc)
    doc_2=set()
    for doc, _ in pos_index[s_w2]:
        doc_2.add(doc)
    com_doc=doc_1 & doc_2  
    ans_docs=set()
    for doc in com_doc:
        p_1=[]
        for d,pos in pos_index[s_w1]:
            if d==doc:
                p_1.append(pos)
        p_2=[]
        for d,pos in pos_index[s_w2]:
            if d==doc:
                p_2.append(pos)
        for p1 in p_1:
            for p2 in p_2:
                if abs(p1-p2)==dist:
                    ans_docs.add(doc)
                    break

    return ans_docs



# All Functions will be called from here in the seuqence


filter_words()
token_stem()


# Calling Inverted Index function to create inv_index dictionary 

inv_index_func()
print(f"Length Of the Inverted Index: {len(inv_index)}")


# Calling Positional Index function to create pos_index dictionary

pos_index_func()
print(f"Length Of the Positional Index: {len(pos_index)}")


my_list=[]
print()

# Calling to process AND/OR/NOT Query
my_list=inv_query()
print(sorted(my_list))
print(f"Length of Result: {len(my_list)}")

print()
# Now Calling to process w1 w1 /n Query
my_list=pos_query()
print(sorted(my_list))
print(f"Length of Result: {len(my_list)}")

print("\n\t\t*** Thanks ***")