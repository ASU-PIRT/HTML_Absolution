# Notes on PHY 101 Lab HTML
These are a series of notes to take into account in the development of the python app to be used in conjunction with the web-app "HTML Washer". 

* HTML Washer: https://www.htmlwasher.com/

This is a temporary solution before a more comprehensive PyScript application is developed.
<br>

## Headers

### <span style="color: darkorange;">Header Order</span>

The tag `<h1>` is shared by **both** the ***main header*** at the top of the page and what is functionally the ***3rd tier header***. Their formatting is identical as well.

    Note: The original document features two formats in the header text. One is unique to the course name portion (eg. PHY 101), the other (the lab title) is shared with the rest of the ***3rd tier*** headers.

    * The course name can remain as `<h1>`, the lab title and the headers should get a different tag.

The `<h3>`is being used for the ***2nd tier*** header that introduces the main body of the document.

The `<h2>` is being used by the ***4th tier*** header, ie. the subsections of the main sections designated by the ***3rd tier header***.

#### To do (in order):
| Banner:
* Remove the `<table>` tags from the banner. (refer to original html washer code.)
* Split the content of `<h1>` into two separate `<h1>` tags.
* remove the `<p>` tag from the `<img>` for the banner image (unnecessary).


| Fixing header tags.
* Change all `<h2>` tags to `<h4>` tags for semantic purposes.
* Change all `<h3>` tags to `<h2>` tags for semantic purposes.
* Replace all `<h1>` after the first into `<h3>` (for semantic purposes).

More notes:
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

Notes on tables:

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

### <span style="color: darkorange;">Proposed Solution</span>

Have the formatting be settled by an accompanying file, such as a .csv created from a spreadsheet like the one created for PHY 132.

* In this spreadsheet include the following:
    * Alt text to be inserted using the `alt=` attribute.
    * A flag for whether an image is a **figure**, a **block equation**, or an **in-line equation**.

* Separate all images that appear in the same `<p>` block container into their own `<div>` containers (or remove containers entirely).

<br>

* If a figure:
    * Insert the html attribute `class="figure"` in the img tag.
    * In the `<p>` tag below (or in its absence: above) the corresponding `<img>` tag, insert the html attribute `class="description"`.
    * *Maybe* create a new block container `<div class='figure-block>` for both formatted into a rows grid, such that the description always appears at the bottom.
* If a block-equation:
    * Insert the html attribute `class="block-equation"` in the img tag.
    * Pair the image with a new inserted block that includes equation number (equation count can be kept track of in python code).
        * Alternatively, an additional flag that includes the number can be created in the .csv file / spreadsheet.
    * Contain both blocks in a unique div tag (user defined) or with `class=block-equation` instead. (Decide between using this for the image or the container.) 
* If an in-line equation:
    * Insert the html attribute `class="inline equation"`

### <span style="color: darkorange;">Background for Equations:</span>

* Make all images in-line blocks.

* Include a white background with a slight alpha value for all of them, eg: `color: rbga(255, 255, 255, 0.5)`.

### <span style="color: darkorange;">Further Notes:</span>

* It may be useful for python scripting to identify the images that are used as blocks (eg. figures and block equations) based on whether they're contained in `<p>` tags themselves. This may facilitate the formatting.