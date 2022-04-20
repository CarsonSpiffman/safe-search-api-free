# safe-content-free
Google SafeContent API Free

API To check if an image is safe or not via Google Cloud without rate limit and free of charge :)

# Example of use
```python
from safe import SafeContentAPI

url = 'https://www.chaty.es/uploads/2021/fotos-de-tetas-amateur-1250.jpg' # NSWF PHOTO
safe = SafeContentAPI(url)
print(safe.get_json())
```

# Response

```
{'results': {'adult': 'VERY_LIKELY', 'spoof': 'VERY_UNLIKELY', 'medical': 'VERY_LIKELY', 'violence': 'VERY_UNLIKELY', 'racy': 'VERY_LIKELY', 
'adultConfidence': 0, 'spoofConfidence': 0, 'medicalConfidence': 0, 'violenceConfidence': 0, 'racyConfidence': 0, 'nsfwConfidence': 0}}
```

Enjoy
