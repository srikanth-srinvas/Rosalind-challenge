#probelem1
import this

# ==== variables and some arithmetic ====== 
a = 964
b = 980
print(f'{a}^2 + {b}^2 = {a**2 + b**2}')

# ===== strings and lists =======

wordOneStartPos = 10
wordOneEndPos = 17

wordTwoStartPos = 89
wordTwoEndPos = 97

txtStr = "hpMtdMVMwyChelydraY5U3VAWhjPosAPXMApNNBz30jmYDv8tGfqD66fuL24Z2wlOpOPYP27D5THokOUIOWUxe2Cxalpestrisnjw8T7Ee8nu2b8o6n0GuHRWH3MxIZSCbl1gAenqQG46NUsxkkgmPpOEAIqmLP9GnTWfY5Wugv."

# Note: end position is not inclusive, so we add 1 to capture it
print(
    f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}')

# ======= conditions and loops ======

startPos = 4506
endPos = 8812
result = 0

for x in range(startPos, endPos + 1):
    if x % 2 != 0:
        result += x

# result = sum(
#     [x for x in range(startPos, endPos + 1) if x % 2 != 0]
# )

print(result)

# ======== working with files =======

input_file_path = '/Users/srikanth/data/scripts/python_scripts/stronghold/python_village/input.txt'
output_file_path = '/Users/srikanth/data/scripts/python_scripts/stronghold/python_village/output.txt'

even_lines = []

with open(input_file_path, 'r') as f:
    lines = f.readlines()
    even_lines = [line.strip() for idx, line in enumerate(lines) if (idx + 1) % 2 == 0]

with open(output_file_path, 'w') as f:
    f.write('\n'.join(even_lines))


# ======== dictionaries ==========

txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# Generic approach:
wordCoutDict = {}

for word in txtStr.split(' '):
    if word in wordCoutDict:
        wordCoutDict[word] += 1
    else:
        wordCoutDict[word] = 1

# Optimized, Pythonic approach, using collections module:
# wordCoutDict = Counter(txtStr.split(' '))

for key, value in wordCoutDict.items():
    print(key, value)