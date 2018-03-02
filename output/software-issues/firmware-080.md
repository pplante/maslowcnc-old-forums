## Firmware 0.80
Posted on **2017-07-14 22:03:06** by **terran**:

Firmware uploaded fine, just wondering if this is going to be an issue?
firmware ver: 0.80
ide ver: 1.8.3
windows ver: 8.1 and 10

sketch\number.c: In function 'bc_str2num':

sketch\number.c:1523:7: warning: assignment discards 'const' qualifier from pointer target type

   ptr = str;

       ^

sketch\number.c:1548:7: warning: assignment discards 'const' qualifier from pointer target type

   ptr = str;

       ^

---

Posted on **2017-07-14 22:16:02** by **gero**:

Hi, I have seen this warning with all firmware so far, but it never seemed to cause an issue.

---

Posted on **2017-07-14 22:43:58** by **terran**:

ok, cool. I saw it as warnings only and compiled ok, so wasn't sure. I won't be able to actually put everything together until next week sometime, but wanted to get the firmware loaded up.

---

