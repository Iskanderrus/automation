import re

phone_pattern = re.compile(r'''(
(\d{,3})\s{1}
(\d{,3}|\(\d{,3}\))
(\s|-|\.)?
\d{,4}
(\s|-|\.)
(\d{4}|\d{2}(\s|-|\.)\d{2})
(\s*(ext|x|ext.|внешн.|доб.)\s* \d{,5}(\s|-|\.)\d{,5})?
)''', re.VERBOSE)

mo = phone_pattern.search('+0 (000) 000-00-00')
print(mo.group())
