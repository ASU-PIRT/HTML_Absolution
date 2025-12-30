# Notes on PHY 101 Lab HTML
<span style="color: brown;">Old: </span>

    These are a series of notes to take into account in the development of the python app to be used in conjunction with the web-app "HTML Washer". 

    * HTML Washer: https://www.htmlwasher.com/

    This is a temporary solution before a more comprehensive PyScript application is developed.
<br>
<span style="color: chartreuse;"> New: </span>

    It is now the intention of this project to create the python scripts from scratch to clean and format the code of HTML documents exported from Google Docs, and eventually other word processing applications, for the use of the ASU Department of Physics.

## Headers

### <span style="color: darkorange;">Header Order</span>

The tag `<h1>` is shared by **both** the ***main header*** at the top of the page and what is functionally the ***3rd tier header***. Their formatting is identical as well.

    Note: The original document features two formats in the header text. One is unique to the course name portion (eg. PHY 101), the other (the lab title) is shared with the rest of the ***3rd tier*** headers.

    * The course name can remain as `<h1>`, the lab title and the headers should get a different tag.

The `<h3>`is being used for the ***2nd tier*** header that introduces the main body of the document.

The `<h2>` is being used by the ***4th tier*** header, ie. the subsections of the main sections designated by the ***3rd tier header***.

#### <span style="color: darkorange;">Solution (in order):</span>
| Banner:
* Remove the `<table>` tags from the banner. (refer to original html washer code.)
* Split the content of `<h1>` into two separate `<h1>` tags.
* remove the `<p>` tag from the `<img>` for the banner image (unnecessary).


| Fixing header tags.
* Change all `<h2>` tags to `<h4>` tags for semantic purposes.
* Change all `</h2>` tags to `</h4>` tags for semantic purposes.

<br>

* Change all `<h3>` tags to `<h2>` tags for semantic purposes.
* Change all `</h3>` tags to `</h2>` tags for semantic purposes.

<br>

* Replace all `<h1>` after the first into `<h3>` for semantic purposes.
* Replace all `</h1>` after the first into `</h3>` for semantic purposes.

#### <span style="color: darkorange;">More notes:</span>
* Headers 3 and 4 have been changed to `display: in-line block` in order to accommodate highlighting.

### <span style="color: darkorange;">Sections & Header Links</span>

Useful functionality for each header is link to its own section. For this reason:

* Each header will create a section that encompasses all of the content that:
    * Uses the header tag as its first line of content.
    * Ends when either:
        * The next header tag / section starts.
        * The parent container ends.
    
* A python script should auto insert the code `<a href=#[insert the container section ID here]>` after the `<h#>` tag and `</a>` before the `</h#>` tag.

<br>

## Tables:

### <span style="color: darkorange;"> Notes on Tables</span>

* For some reason, every `<td>` entry includes `<p>`. These should probably be deleted.
    * The entries also have attributes for column and row size. I guess it can't hurt.
* First row should be used be table headers and should therefore use the tag `<th>` instead of `<td>` for formatting purposes.<br>

* Table label appears after table designated by just a `<p>` tag.
    * It would probably be convenient to organize the table label to be part of the table tag.
    * The caption tag limits the width of the text, therefore it may not be appropriate or useful for a description tag solution.
        * ~~Try `max-width="none"` ?~~
    * The `<p>` tag following the table's closing tag `</table>` could be given a special class attribute such as `class="description"`.
        * Add `<b>` tags around text up until the first colon, eg. `<b>Table 1:</b>
        * This solution should work the same for images and labels!

* The tags `<thead>`, `<tbody>`, `<tfooter>` are not present in the table. They can can probably be used for formatting purposes.



* <span style="color: Chartreuse;">***New!***</span> It is convenient to also include tables in the block-figure class for formatting purposes. Should there be a reason to make a separate "block-table" class. It should be noted here.

## Images:

### <span style="color: darkorange;">Image Formatting:</span>

Notes on image formatting:

* Not all images are neatly scaled by default.
    * Perhaps python code can be developed to automatically add file accurate width and height html attributes for the image tags.
* Python script could be develop to fill in alt text from a file based on the image name.

* Some image description appear ***above the image***, *unlike tables*.
    * Image descriptions could use the same `class="description"` tag attribute for css formatting, but may require a different method to identify in python code.
    * As suggested above, some image descriptions still appear **after** the image tag for some reason.
    * All descriptions should be under the images.

* Some images that are meant to be separate appear in the same `<p>` block container.

<br>

* Some images are <mark>equations</mark>.
    * Some equations appear in-line, and not as designated special equations.
    * Equations that do appear as block, designated equations do not require descriptions, but could use a parenthesis number to the right. (Grid solution?)

* Some images have a transparent background, so including a white background with some alpha may be useful for accessibility reasons.

* <span style="color: Chartreuse;">***New!***</span> It would be nice if every block figure, table, and equation had an automatically created ID that it both links to and can be referred to throughout the document.

## For Both Tables and Figures

### <span style="color: darkorange;">Proposed Solution</span>

Have the formatting be settled by an accompanying file, such as a .csv created from a spreadsheet like the one created for PHY 132.

* In this spreadsheet include the following:
    * Alt text to be inserted using the `alt=` attribute.
    * A flag for whether an image is a **figure**, a **block equation**, or an **in-line equation**.

* Separate all images that appear in the same `<p>` block container into their own `<div>` containers (or remove containers entirely).

<br>

* If a **figure** (or ***table***):
    * Insert the html attribute `class="figure"` in the img tag.
    * In the `<p>` tag below (or in its absence: above) the corresponding `<img>` tag, insert the html attribute `class="description"`.
    * *Maybe* create a new block container `<div class='figure-block>` for both formatted into a rows grid, such that the description always appears at the bottom.
* If a **block-equation**:
    * Insert the html attribute `class="equation-block"` in the img tag.
    * Pair the image with a new inserted block that includes equation number (equation count can be kept track of in python code).
        * Alternatively, an additional flag that includes the number can be created in the .csv file / spreadsheet.
    * Contain both blocks in a unique div tag (user defined) or with `class=block-equation` instead. (Decide between using this for the image or the container.) 
* If an **in-line equation**:
    * Insert the html attribute `class="inline equation"`

<br>

* <span style="color: Chartreuse;">***New!***</span> Using Python, give every **block equation**, **table**, and **figure** have an automatically generated ID attribute.<br>

    * Said ID can be taken from:
        * the description tag that is in the same container.
        * the csv document flag.
        * a python variable that tracks the number of instances of each category.
        * If multiple of these solutions are adopted, devise a way to resolve conflicts by giving an order of priority.

    * It would also be useful for **block images** to link to themselves.
        * insert a ``<a href="#[insert ID here]>`` tag before every ``<img>`` tag
        * insert ``</a>`` after every ``</img>`` tag.



### <span style="color: darkorange;">Background for Equations:</span>

* Make all images in-line blocks.

* Include a white background with a slight alpha value for all of them, eg: `color: rbga(255, 255, 255, 0.5)`.

### <span style="color: darkorange;">Further Notes:</span>

* It may be useful for python scripting to identify the images that are used as blocks (eg. figures and block equations) based on whether they're contained in `<p>` tags themselves. This may facilitate the formatting.

## Text Formatting

### <span style="color: darkorange;"> Notes on Formatting </span>

* HTML Washer does not automatically transfer any ***bold***, ***italics***, or ***underline*** (also ***highlight***) tags that may be present in the original document.

* Block figure descriptions originally appear in bold, so there may be some benefit in automatically detected and applying bold tags. Alternatively, whatever solution devised must not be to the detriment of the solutions for the block figure formatting.

* There is no simple and appropriate method (that I can think of) to automatically turn generic styling tags such as `<b>`, `<i>`, and `<u>` into semantically meaningful ones such as `<strong>`, `<em>`, and `<strike>`.
    * The application of semantically meaningful stylization tags would most likely require manual evaluation.
    * Refer to an HTML guide for a list of semantically meaningful tags that may be useful.

#### <span style="color: darkorange;"> Proposed Solution </span>

* ✅ Investigate the original document export. Identify if there is consistency for the formatting tags corresponding to each: ***bold***, ***italics***, or ***underline***, and any combination thereof.

* ✅ Investigate whether HTML Washer eliminates generic styling tags like `<b>`, `<i>`, and `<u>`.

    * <span style="color: Chartreuse;">***New!***</span> HTML Washer does not eliminate generic tags. It's Google Docs that does not employ these tags in their HTML export, opting instead of creating arbitrary classes ad hoc to handle the stylization at the CSS level.

    * If there is consistency & HTML Washer does **NOT** eliminate generic tags:
        * Create a script that automatically replaces the export tag with the generic tag.
    
    * <span style="color: brown;">Obsolete</span> <span style="color:gray">If there is consistency & HTML Washer eliminates generic tags:</span>
        * <span style="color:gray">Create a script that identifies phrases that feature formatting that can't be otherwise automatically formatted (eg. description elements), such that they are easily manually searchable (ctrl+f).</span>
        * <span style="color:gray">Identify which part of the phrase requires the tags.</span>
        * <span style="color:gray">Create a flag for what kind of stylization the phrase requires (*eg. bold, italics, underlyng, or any combination thereof*).</span>
        
        <br>

        * <span style="color:gray">Manually review the document an manually insert the appropriate semantic tags based on context (*eg. strong, em, strike, or any combination thereof*)</span>

            * <span style="color:gray"><span style="color: darkorange; font-weight: bold;">Note!</span> This process may still be useful for the inclusion of appropriate semantic tags even if the inclusion of generic tags can be automated.</span>

#### <span style="color: darkorange;"> <span style="color: Chartreuse;">***New!***</span> Notes on Implementation

* CSS tags:

    * Google Docs creates a set of arbitrary classes that handle all the stylization of in the document at the CSS level (there is not `<b>` tags in the html, for example, instead something like `<span class="c14">`).

        * A significant number of these tags do not even include any content, and are just used for line spacing and stuff.

    * It is <strike style="color: gray">likely</strike> **confirmed** that all of these classes are ad hoc and are not shared across different documents.
        * It is going to be important to identify the css declarations that create the basic styling functions. These are the following:
            * ***Bold*** : `font-weight:700`
            * ***Italics*** : `font-style:italic`
            * ***Underline*** : `text-decoration:underline` 
            
            <br>

            * *Highlight* : `background-color:` 
                * Finding specific highlighted text is going to be less useful since headers, the page heading, and tables use specific background colors that would be identified.
                * There aren't any instances of highlighted text in the way that the `<mark>` tag would use.
        
<br>

## Ordered & Unordered Lists

### <span style="color: Chartreuse;">***New!***</span> <span style="color: darkorange;">Notes on Bolding</span>

* Unordered lists tend to have first item be bold.
* For all list items:
    * If the line includes a `:`, then all of the text before the LAST `;` will be **bold**, any text after will **NOT**.
* Unfortunately, there *isn't* a convenient css formatting tool that formats all of the text before a character, so therefore the python script will have to do the formatting.
    
#### <span style="color: Chartreuse;">***New!***</span> <span style="color: darkorange;">Proposed Solution</span> (please review)

* For only `<ul>` elements of the first order, IF the element does not include a `;` element:
    * all direct `<li>` children will be set bold by default.
* For all `<li>` elements, if it includes the `;` character:
    * ***HTML option:*** the `<b>` tag will be inserted after the `<li>` tag and the `</b>` tag will be inserted after the `;` character.
    * ***CSS Solution:*** Use the python script to create `<span>` tags instead with a `class=imperative` attribute, and do the formatting in CSS.

### <span style="color: red;">***CRITICAL!***</span> <span style="color: darkorange;"> Improper Google Docs List Import </span>

#### <span style="color: Chartreuse;">*New!*</span> <span style="color: darkorange;"> Google Stinks </span>

        It turns out Google ... , and the bulleting in ordered and unordered lists does not use proper tiering in their HTML export. Instead, all of the formatting happens at the CSS level. ***How awful.***

#### <span style="color: Chartreuse;">*New!*</span> <span style="color: darkorange">LibreOffice HTML Formatting</span>

* Exporting a google doc document into .odt does not seem to work as of now.

* Exporting into .docx and opening LibreOffice works very well.
    * An exception is that all graphics developed in Google Docs "draw" feature itself do not render or appear correctly.

* From LibreOffice, there are two ways of getting HTML code:
    * Send -> Create HTML
        * **Do not use this.** 
            - The only useful thing that it does is export the images.
            - It creates multiple files for different sections of the page.
    * <span style="color: Chartreuse;">**Create HTML preview & View Page Source**</span>:
        + +This works very well.
        + +It maintains proper list formatting in HTML.
        + +It maintains style formatting.
        - -All of the images are formatted as temp files, so there is no convenient export.
        - -Creating the script based on this would necessitate a manual overview of all image files. This would be overly cumbersome because:
            - All equations are rendered as image files
            - All google doc "draw" images combine image and text formatting.
* <span style="color:red">**Sadly.**</span> Using LibreOffice for this solution would be too cumbersome for myself and, especially, any other user. Therefore, this document is now entirely made to address google docs.
* Wine and Proton are made in spite of Windows, so I'm in good company.

#### <span style="color: Chartreuse;">*New!*</span> <span style="color: darkorange">Identifying Bullet Tier from CSS tags</span>
* Never mind everything else. It is fairly trivial to identify what css tags google exports to make the different bullet tiers.
* From an initial observation, Google formats the tiers from the `<ul>` tag in the following way:
    * 1st tier: `lst-kix_cprgjs9jt2l2-0`
        * `content:"\0025cf "` , black circle
    * 2nd tier: `lst-kix_cprgjs9jt2l2-1 start`
        * `content:"\0025cb"` , white circle
    * 3rd tier: `lst-kix_cprgjs9jt2l2-2 start`
        * css introduces the character: `\0025a0` which is a black square
    * 4th tier (never used) `lst-kix_cprgjs9jt2l2-3`:
        * `content:"\0025cf "`
        * it re-uses the same character as first tier.
        * as far as I can tell, the only thing that distinguishes this from the 1st tier tag is the `-3` ender in the tag
* They also include the class `c3` for some reason.
* The `start` portion seems to only apply for counter-reset options so it may be irrelevant for unordered lists.


<br>

## Formatting HTML Python Script Outline

### <span style="color: Chartreuse;">*New!*</span> <span style="color: darkorange;">HTML Line Breaks and Indentation</span>

The first step is going to be to turn all of the export code into readable code. To do so:

* Identify all element tags that require a line break.
    * These will be the tags for block elements.
    * This also be block and configuration void elements, such as `<!DOCTYPE html>` and `<meta>`.
        * Insert `\n` newline code in python after the closing character or tag.

* Develop method to identify nesting level and indent each newline accordingly.
    * Initiate variable `nest_tier=int(0)` that determines the nesting tier as an integer.
        * The value of the nesting tier will be determine the number of instances of non-breaking space characters to be inserted after every newline created multiplied by the variable `tier_indent=int(2)`.

    * For all block elements (except `<p>`) opening tags:
        1. add +1 to `nest_tier`
            * `nest_tier += 1`
        2. add a newline with `\n`
        3. insert `&nbsp` by a multiple of `nest_tier`.

Apply solution.

### <span style="color: Chartreuse;">*New!*</span> <span style="color: darkorange;">CSS Line Breaks and Indentation</span>



