import re
def clean(text):
    #'''Clean text by removing unnecessary characters and altering the format of words.'''
    text = text.lower()
    
    text = re.sub(r"(\s+)", " ", text)
    text = re.sub(r"_", " ", text)
    text = re.sub(r"(\*+)", " ", text)
    text = re.sub(r"[-%^()\"#/@;:<>{}`+=~|!,]", " ", text)
    text = re.sub(r"  ", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text
def preprocess_sent(sent1,sent2):
    sent1=clean(sent1)
    sent2=clean(sent2)
    return sent1,sent2
def preprocess_word(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    word1=re.sub(r"[-%^()\"#/@;:<>{}`+=~|!,]", "", word1)
    word2=re.sub(r"[-%^()\"#/@;:<>{}`+=~|!,]", "", word2)
    #word1=re.sub(r"[0-9]", "", word1)
    #word2=re.sub(r"[0-9]", "", word2)
    return word1,word2

def compare_w2w(sent1_words,sent2_words):
    
    m_count=0
    for word1 in sent1_words:
        for word2 in sent2_words:
            if word1==word2:
                m_count+=1
    avg_words=(len(sent1_words)+len(sent2_words))/2
    match_ratio=(m_count/avg_words)*100
    return match_ratio
    
def compare_a2a(word1,word2):
    m_count=0
    word1,word2=preprocess_word(word1,word2)
    min_length=min(len(word1),len(word2))
    for i in range(min_length):
        for j in range(min_length):
            if word1[i:i+j] in word2:
                m_count+=1
    if min_length!=0:
        ratio=((m_count/min_length)/min_length)*100
        #print(word1+" vs "+word2+" Match ratio "+ str(ratio)+"%")
        #print()
        return ratio
    else:
        return 0
    
    
def compare(sent1,sent2):
    sent1,sent2=preprocess_sent(sent1, sent2)
    sent1_words=sent1.split()
    sent2_words=sent2.split()
    w2wmatch_ratio=compare_w2w(sent1_words, sent2_words)
    a2amatch_ratio=0       
    #print(sent1_words)
    #print(sent2_words)
    min_word_length=min(len(sent1_words),len(sent2_words))
    for i in range(min_word_length):
        a2amatch_ratio+=compare_a2a(sent1_words[i], sent2_words[i])
    try:
        a2atotal_mr=a2amatch_ratio/min_word_length
        final_match_ratio=(w2wmatch_ratio+a2atotal_mr)/2
        return final_match_ratio
    except:
        return 0   
      
def compare_2_words(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    match=0
    len1=len(word1)
    len2=len(word2)
    min_len=min(len1,len2)
    max_len=max(len1,len2)
    for i in range(min_len):
        if word1[i]==word2[i]:
            match=match+1
        else:
            if word1[i] in word2:
                match=match+1
    match=int((match/max_len)*100)
    return match

s1=input("enter first sentense ")
s2=input("enter second sentense ")
match=int(compare(s1,s2))
print("match ratio is {} %".format(match))


           
           
           
           
