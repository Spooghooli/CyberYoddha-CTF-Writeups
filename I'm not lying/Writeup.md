# I'm not lying challenge

We are given the file platypusBear.mp3 and are asked to find the flag hidden inside it

If we insert the file into ![Audacity](https://www.audacityteam.org/), and switch to spectogram view

![image](https://user-images.githubusercontent.com/70701563/98003879-ee798100-1df7-11eb-824f-8320bee7eda9.png)

If we scroll to the point between 12.70 and 14.20 we can see something interesting

![image](https://user-images.githubusercontent.com/70701563/98005043-4ebcf280-1df9-11eb-9f1b-0de6863fa40f.png)

This looks like morse code, so I try to clear it up a bit using the vocal removal, low pass and high pass effects consecutively we get something like this:

![image](https://user-images.githubusercontent.com/70701563/98039392-4da2ba00-1e27-11eb-8826-322e9b5b0c20.png)

Decoding the morse code with a bit of eye strain we get: cyctf{tru7h_h1dd3n_und3r_l!e$}
