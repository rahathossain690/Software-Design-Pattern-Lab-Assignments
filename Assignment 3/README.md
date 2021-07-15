# Assignment 3
Python code for assignment 3. This code uses the adapter, the singleton and the abstract factory design pattern.

# Installing
1. Install nodejs and npm.
```
npm install
```
3. Run 
```
node Solution32.js
```

# Problem description
The problem is to design a modern User Interface (UI) that supports multiple design styles (motif
or ”look and feel”). The core of the UI is the single Window Manager (WM), which is
responsible for the management of the UI items, such as buttons, text boxes and edit boxes.
Different design styles are supported by the system: simplistic design style(for example, we can
change the color of the elements), high detailed design style(for example, we can change the
color and text size of the elements). WM should be initialized only by specifying the design
style. Each UI item looks differently when the design style of the system is different. Also, each
item has a value, which is displayed on the item itself (i.e. value of a button is the text displayed
on the button).
The structure of a UI is described in a special config file. This file contains the structure of a UI
as a list of UI items, their values and their coordinates. Example of a config file:
Button, Click on me, X: 250, Y: 300
EditBox, Some text to edit, X: 250, Y: 350
…
A Config Manager class is responsible for loading config files. It has methods nextItem() -
returns the next item in the list and hasMoreItems() - returns true if iterating through the list is
not over yet. Window Manager has a method loadUI(ConfigManager config), which goes
through the config step by step and displays all UI items.
To extend the functionality of the system, it must also be possible to load the configuration from
an XML file. Your application should adapt one of the native java XML parsing methods (DOM
Parser/Builder, SAX Parser, Java XML I/O) and make it compatible with the ConfigManager
interface. Example of an XML file:
<Button value=“Click on me” X=“250” Y=“300” />
<EditBox value=“Some text to edit” X=”250” Y=“350” />
...

Finally, to test the system, load UI elements from a config file, then from an XML file and then
create several items during the runtime programmatically.


# File Structure
1. ClassDiagram32.png
2. config.any: any config file/ basically csv.
3. config.xml
4. Highly Detailed System demo 32.png
5. Simplistic System demo 32.png
6. Solution32.js: Main solution in javascript
7. package.json: npm package registry
8. SDP_Assignment_TaskThree.docx: Project assumption