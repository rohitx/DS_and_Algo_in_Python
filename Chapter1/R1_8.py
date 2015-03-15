'''
R-1.8: Python allows negative integers to be used as indices into a sequence,
as a string. If string s has length n, and expression s[k] is used for index
-n<k<0, what is the equivalent index j >= 0 such that s[j] references the
same element.

Answer: For a given string of length n, the last index is the length
of the string. Hence, s[-1] == s[len(n) - 1]. Similarly, the first index is,
s[-len(n)] == s[0]. Therefore, s[k] == s[len(n) - k], where j = len(n) - k.
'''
