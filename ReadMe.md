<h1 align="center">Emilion</h1>
<br>

This project is made for learning but also for the challange. It should not be neccesary to leave the running program mostly. Although this won't be the case exactly as many things are very hard to implement. This is planned to become a Mini-Desktop.

<h2>Features</h2>
<br>

<b>Ice Menu</b> <br>
This is where all the applications that can be used are listed. The Menu can be hidden at any time by dragging the slider to the left side. <br> Here is a list of those applications.
<ul>
  <li>Starting page</li>
</ul>

<b><u>Fire Menu</u></b> <br>
This is where the current application will get displayed.

<h2>How to install Tkinter</h2>
<br>

With these commands you can install Tkinter and run any Program using the Tkinter library from the Terminal

<b>1. macOS</b>
<ul>
  <li>brew install python-tk</li>
</ul>

<b>2. Linux (Arch)</b>
<ul>
  <li>sudo pacman -S tk</li>
</ul>

<h2>Why is everything in one file</h2>
<p>
  Because importing a class with drawing graphics will only be able to draw on a fixed surface (at specific location).
  This is not what I want.
  I want the graphics to attach to the right frame.
  Classes can't access the main file from their location.
  So I need to use this hack for it work properly and for me to be able to scale everything up.
  This is how it's gonna be till I find a better way.
</p>
