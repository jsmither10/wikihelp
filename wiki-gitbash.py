
import wikipedia
import sys

result = wikipedia.page("Louisville Kentucky")
#print(result.summary)
#print(result.summary.encode('utf-8').decode('utf-8'))

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
print(result.summary)
