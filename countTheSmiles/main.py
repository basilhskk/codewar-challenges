# Count the smiley faces!
# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python 

def count_smileys(arr):
    ans = 0 
    eyes = [":",";"]
    noses = ["-","~"]
    smiles =[")","D"]
    for face in arr:
        parts = list(face)
        if(len(parts)==2):
            if parts[0] in eyes and parts[1] in smiles:
                ans= ans +1
        if (len(parts)==3):
            if parts[0] in eyes and parts[1] in noses and parts[2] in smiles:
                ans = ans +1
    return ans



count_smileys([';]', ':[', ';*', ':$', ';-D'])