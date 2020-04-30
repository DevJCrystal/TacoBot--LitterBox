# TacoBot--LitterBox
Automated LitterBox using Raspberry Pi and Stepper Motors

I will be creating sections and they will have a last update field per section. 

---
About the project:
Hello!
I got two cats in Januray of 2020. When picking out the supplys for them, I saw the large collection of automated litterboxes. All costing a pretty penny. I understand it would be making my life easier by purchasing them but I knew I could probably make it myself. I was hoping it would be cheaper but I also don't really know much about how much torque I would need and how much it was going to weigh. I just had the idea. And I wanted to start the project. So the price list below will change as I learn. 

The code.. This is my first time really publishing my code. I have not taken any classes with Python or really any other programming language. Mostly self taught through trial and error with some youtube in there. As of the time I am writing this, the code has very minimal error checking and bugging. Not one error log.. but they will come! Logs are great but I have a bunch of projects I am working on so I am kinda going back and fourth.

If you have any suggestions or questions, please feel free to let me know. Let's make this an awesome DIY automated cat litter box. 

---
Progress:
Last Update: April 29th, 2020

1. MotorController completed
2. Basic webpage completed
3. Android app that connects to webpage completed
4. Daily Scheduler completed
Wait for parts..
---
Android App (Source included):
Last update April 30, 2020
https://photos.app.goo.gl/1skhdcaWTBMKo6N39
---
Parts:
Last Update: April 29th, 2020

0. 16 Gb SD Card | https://www.amazon.com/Sandisk-Ultra-Micro-UHS-I-Adapter/dp/B073K14CVB/ref=sr_1_4?dchild=1&keywords=16+gb+sd+card&qid=1588182071&s=pet-supplies&sr=1-4-catcorr
1. Raspberry Pi 3 | https://www.amazon.com/s?k=raspberry+pi+3&ref=nb_sb_noss
2. Raspberry Pi Stepper HAT | https://www.adafruit.com/product/2348
3. (2x) Stepper Motors | https://www.amazon.com/gp/product/B01N30ISYC/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
* The second stepper motor can be a smaller motor to save some money.
4. Stepper Belts (In testing) | 
5. LitterBox | https://www.amazon.com/gp/product/B073GVRT8V/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1

Approx Cost: $160 (Seems with Covid, the prices are going up)
Learning experence and fun: Priceless

---
Waiting on my 3D printer to arrive.

When I get the printer, I will create a second list for those with printers.  
---
Setting up the pi

Last updated: April 30th, 2020

The Main script is WebServer.py so we need to set it to start with the pi.

Once you are logged in, enter "sudo crontab -e"

At the bottom, you will need to type

@reboot python3 /home/pi/Scripts/WebServer.py &

Adjust the above to the location of the project.

sudo reboot

Once you are back up, try connecting to the webpage your pi.

---
Assembly: TBD
Last Update: April 29th, 2020
---
