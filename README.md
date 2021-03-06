# Forked project

## Changes
The main change from the original project is the addition of two files to the RegexGenerator/ConsoleRegexTurtle/dist folder. consoleregexturtle.py and consoleregexturtle.html

### consoleregexturtle.html
A simple HTML/JS file where one can load a raw text file, and highlight words and generate a JSON file to be used with the consoleregexturtle jar file. 

### consoleregexturtle.py
A simple py file where one can pass file containing a line seperated list of words. The output is either stdout or a JSON file which can be used with consoleregexturtle jar file.

### Usage (command line tool)
```text
java -jar ConsoleRegexTurtle.jar -d regex_dataset.json
```

```text
java -jar ConsoleRegexTurtle -t 4 -p 500 -g 1000 -e 20.0 -c "interesting evolution" -x true -d dataset.json -o ./outputfolder/

On linux you can invoke this tool using the alternative script:
regexturtle.sh -t 4 -p 500 -g 1000 -e 20.0 -c "interesting evolution" -d dataset.json -o ./outputfolder/

Parameters:
-t number of threads, default is 2
-p population size, default is 500
-g maximum number of generations, per Job, default si 1000
-j number of Jobs, default si 32
-e percentange of number generations, defines a threshold for the separate and conquer split criteria, when best doesn't change for the provided % of generation the Job evolution separates the dataset.
   Default is 20%, 200 geberations with default 1000 generations.
-d path of the dataset json file containing the examples, this parameter is mandatory.
-o name of the output folder, results.json is saved into this folder; default is '.'
-x boolean, populates an extra field in results file, when 'true' adds all dataset examples in the results file 'examples' field, default is 'false'
-s boolean, when 'true' enables dataset striping, striping is an experimental feature, default is disabled: 'false'
-c adds an optional comment string
-h visualizes this help message

Dataset path is needed.
Usage:
java -jar ConsoleRegexTurtle -t 4 -p 500 -g 1000 -e 20.0 -c "interesting evolution" -x true -d dataset.json -o ./outputfolder/

On linux you can invoke this tool using the alternative script:
regexturtle.sh -t 4 -p 500 -g 1000 -e 20.0 -c "interesting evolution" -d dataset.json -o ./outputfolder/
```

# RegexGenerator

This project contains the source code of a tool for generating regular expressions for text extraction and classification (flagging):

1. automatically,
2. based only on examples of the desired behavior,
3. without any external hint about how the target regex should look like.

An online, interactive version of this engine is accessible at: [http://regex.inginf.units.it/](http://regex.inginf.units.it/)

RegexGenerator was developed at the [Machine Learning Lab, University of Trieste, Italy] (http://machinelearning.inginf.units.it).

The provided engine is a developement release (1) that implements the algorithms published in our articles (2):

* Bartoli, De Lorenzo, Medvet, Tarlao, Inference of Regular Expressions for Text Extraction from Examples, IEEE Transactions on Knowledge and Data Engineering, 2016
* Bartoli, De Lorenzo, Medvet, Tarlao, Can a machine replace humans in building regular expressions? A case study, IEEE Intelligent Systems, 2016
* Bartoli, De Lorenzo, Medvet, Tarlao, Virgolin, Evolutionary Learning of Syntax Patterns for Genic Interaction Extraction, ACM Genetic and Evolutionary Computation Conference (GECCO), 2015, Madrid (Spain)

More details about the project can be found on [Machine Learning Lab news pages](http://machinelearning.inginf.units.it/news/newregexgeneratortoolonline).

We hope that you find this code instructive and useful for your research or study activity.

If you use our code in your reasearch please cite our work and please share back your enhancements, fixes and 
modifications.

## Project Structure

The RegexGenerator project is organized in three NetBeans Java subprojects:

* ConsoleRegexTurtle:  cli frontend for the GP engine
* MaleRegexTurtle:       provides the regular expression tree representation
* Random Regex Turtle:     GP search engine 

## Other Links

Machine Learning Lab, [Twitter account](https://twitter.com/MaleLabTs)

RegexGenerator [wiki](https://github.com/MaLeLabTs/RegexGenerator/wiki) with installation walkthrough and guide

---

(1) This is a developement version branch which *slightly* differs from the cited works.

(2) BibTeX format:

    @article{bartoli2016inference, 
	  author={A. Bartoli and A. De Lorenzo and E. Medvet and F. Tarlao}, 
	  journal={IEEE Transactions on Knowledge and Data Engineering}, 
	  title={Inference of Regular Expressions for Text Extraction from Examples}, 
	  year={2016}, 
	  volume={28}, 
	  number={5}, 
	  pages={1217-1230}, 
	  doi={10.1109/TKDE.2016.2515587}, 
	  ISSN={1041-4347}, 
	  month={May},
    }
    @inproceedings{bartoli2015evolutionary,
      title={Evolutionary Learning of Syntax Patterns for Genic Interaction Extraction},
      author={Bartoli, Alberto and De Lorenzo, Andrea and Medvet, Eric and
      Tarlao, Fabiano and Virgolin, Marco},
      booktitle={Proceedings of the 2015 on Genetic and Evolutionary Computation Conference},
      pages={1183--1190},
      year={2015},
      organization={ACM}
    }
    @article{bartoli2016can,
      title={Can a machine replace humans in building regular expressions? A case study},
      author={Bartoli, Alberto and De Lorenzo, Andrea and Medvet, Eric and Tarlao, Fabiano},
      journal={IEEE Intelligent Systems},
      volume={31},
      number={6},
      pages={15--21},
      year={2016},
      publisher={IEEE}
    }

