f=open('sample.txt','r')
punctuations = '!()-[]{};:\'"\,<>./?@#$%^&*_~'
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
cont=f.read()
words=cont.split()
words_dic={}
for i in words:
    hi=(i.strip('!()-[]{};:\'"\,<>./?@#$%^&*_~')).lower()
    
    if hi.isalpha() and len(hi)>2:
        if (hi not in uninteresting_words) :
            
            if hi in words_dic:
                words_dic[hi]+=1
            else:
                words_dic[hi]=1
print(words_dic)
f.close()
