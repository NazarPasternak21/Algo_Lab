def rabin_karp(haystack, needle):
    if not haystack or not needle:
        return []

    prime = 101
    base = 256

    m = len(needle)
    n = len(haystack)

    needle_hash = 0
    haystack_hash = 0

    for i in range(m):
        needle_hash = (needle_hash * base + ord(needle[i])) % prime
        haystack_hash = (haystack_hash * base + ord(haystack[i])) % prime

    indices = []

    for i in range(n - m + 1):
        if needle_hash == haystack_hash and haystack[i:i + m] == needle:
            indices.append(i)

        if i < n - m:
            haystack_hash = (base * (haystack_hash - ord(haystack[i]) * pow(base, m - 1, prime)) + ord(
                haystack[i + m])) % prime
            haystack_hash = (haystack_hash + prime) % prime
    
    return indices


haystack = "ababcababcabcabc"
needle = "abc"
result = rabin_karp(haystack, needle)
print("Індекси входжень:", result)
