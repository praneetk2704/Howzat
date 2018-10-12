# Howzat
Howzat is a Python script to show Windows 10 toast notifications for live cricket scores. As of now, the script supports only the Windows 10 platform. Further updates to make it Linux compatible will be added soon.
You can get toast notifications whenever a four or six is hit, wicket is taken or at the end of an over which can be customized as per the user's needs. <br /><br />
Demo video of the script : https://drive.google.com/open?id=11JH25moj6pen4UwQSc_XKZQICzpzR5iB <br /><br />
![four](https://user-images.githubusercontent.com/29803330/46859573-b75c5f80-ce2b-11e8-8d24-830ac8b2f9c6.jpg) &nbsp; &nbsp; &nbsp; &nbsp;
![six](https://user-images.githubusercontent.com/29803330/46859575-b9beb980-ce2b-11e8-8818-5a0117cb528e.jpg) <br /><br />
![wicket](https://user-images.githubusercontent.com/29803330/46859577-bc211380-ce2b-11e8-88e4-359d3881c9ad.png) &nbsp; &nbsp; &nbsp;
![over](https://user-images.githubusercontent.com/29803330/46859582-be836d80-ce2b-11e8-9538-c7903e717837.jpg) <br /><br />


## Working

First of all, you'll be needing Chromedriver. <br />
Download Chromedriver from here : http://chromedriver.chromium.org/downloads. <br />
After downloading Chromedriver, unzip the file and copy the path of 'chromedriver.exe' in line 38 of 'Howzat.py'.
![image](https://user-images.githubusercontent.com/29803330/46860319-ce03b600-ce2d-11e8-8baf-760ab0e6e521.png)

All set and done, now you'll only need to provide the user input for the script.

The most important parameter of the input is the URL of the match, which is basically the URL of the commentary section of the match on Cricbuzz. For eg., for the current India vs West Indies test match, the URL can be found as follows.
1. Head over to https://www.cricbuzz.com/cricket-match/live-scores.
2. On the top part of the page, you'll be able to find a list of matches like this. <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46862332-3fddfe80-ce32-11e8-810e-4d7ca49f3520.png) <br /> <br />
3. Click on the match for which you want the scores. Eg., here we click on 'IND vs WI - Live'. <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46862734-2be6cc80-ce33-11e8-857b-c07ce5251ae6.png) <br /> <br />
4. After this, we get a page something like this. <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46862843-6ea8a480-ce33-11e8-86a8-73b2d625406f.png) <br /> <br />
5. The URL of this page is our required input. <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46862947-bc251180-ce33-11e8-8b5b-858a930b8731.png) <br /> <br />
6. Paste this URL in line 14 of 'Howzat.py'. <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46863091-1920c780-ce34-11e8-96bb-ea38e44349b7.png) <br /> <br />

**NOTE : Obviously this is not the only method to get our URL, but keep in mind to always use the URL of the 'Commentary' section, not of 'Scorecard' or 'Full Commentary' or any other sections, because getting the URL correct is the most important part.**

![image](https://user-images.githubusercontent.com/29803330/46863347-d3b0ca00-ce34-11e8-935d-4e8d854b44ae.png) <br /> <br />

After getting the URL, we need to enter the following inputs :
1. **time_interval** : In seconds. It is basically the amount of time after which the script will crawl the page again to fetch the latest scores. Keeping it at a low value will lead to faster score updates and keeping it at a higer value will lead to delayed score updates. However, it is advised to keep it at a value >= 10. Recommended : 15. <br /> <br />
Now, for the next 5 inputs, we only need to specify either a 'Y' or 'N'. <br /> <br />
2. **show_match_status** : Match status is whatever appears in red on the scores page. <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46863840-2343c580-ce36-11e8-83e2-9edb52e936f3.png) <br /> <br />
Since the primary notification did not have enogh space to show the match status, it appears as a second notification just after the primary one. <br /> <br />
![screenshot_1](https://user-images.githubusercontent.com/29803330/46863950-83d30280-ce36-11e8-927b-85c1a897b38e.jpg) <br /> <br />

3. **show_fours** : Whether you want the notifications after a four is hit.
4. **show_sixes** : Whether you want the notifications after a six is hit.
5. **show_wickets** : Whether you want the notifications after the fall of a wicket.
6. **show_EndOfOver** : Whether you want the notifications after the end of an over.

**SAMPLE USER INPUT** <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46864572-70289b80-ce38-11e8-97ea-948523ba773e.png) <br /> <br />

**NOTE : You can also set the icon which appears along with the notifications. For the cricket icon, download 'Cricket.ico' from this repository and copy it in the same path as the script. For your own custom icons, download a .ico file from the internet and set it's path in the 'toaster.show_toast()' in lines 119, 123, 143 and 147 of 'Howzat.py' under the argument 'icon_path'.** <br /> <br />
![image](https://user-images.githubusercontent.com/29803330/46865320-c1398f00-ce3a-11e8-8e6e-374ad72eb8c6.png) <br /> <br />
That's it. You can cheer for your favourite team now!! :)
