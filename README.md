My graduation theses

This work aims to understand and process data about NHL players. 
With data, we create a prediction model to players salary. 
The full analytical process will be implemented with the CRISP-DM in Python. 
With Feature selection we find the most influencing attributes, with Stepwise regression we find the best combina-tion of attributes.
And with Polynomial regression, we calculate the final model. 
From multiple iterations, we choose the best model. 
This model used a support application. 
This application will be created using a combination of R and Python programming languages. 
The final version of the app will be tested and evaluated user testing.

Business understanding

Our goal was to create multiple models that will predict the salary of NHL players. 
From these models, we choose the best one with the potential to be deployed into practice in the form of a web application. 
From the analytical point of view, we aimed at a selection of the most important attributes affecting the players’ salary and based on this selection; we applied the regression algorithms.

Data Preparation

Most of the attributes are of numeric type. 
Nominal types are BIO attributes such as name, surname or country. 
We divided the goalie's stats into ten and player’s stats into 12 categories by the same characteristics. 
In the beginning, the number of attrib-utes was high and therefore, depending on the correlation between them, we started their reduction. 
  For example, the pairs of attributes like iFOW – Fow.Up, G.Tip – G.Wrap, iPent – iPENT or Misc – G.Misc represents a situation that one of them is calculated from the value of the second. 
We also used the Bayesian information criterion (BIC) to remove less-important categories and keep only relevant data.
Next, we needed to synchronize the attribute names and to determine one measur-ing unit. 
Also, we have removed all players and goalies that have played 9 or fewer matches. 
Then we created new 12 attributes based on existing data. 
Next, we divided the data into nine tables by type of contract and by the player's position. 
Goalies data was split into three small sub files by contract type to RFA (restricted free agents), UFA (unrestricted free agents) and rookie categories with salary less than 1 million.
Player attributes were initially divided by position, namely to the defenders and the forwards. 
Then again by contract type to UFA, RFA and rookie with salary less than 1 million. 
Overall, we have 9 data files. The goalies samples contained 47 columns and 62-261 rows, the players’ data 59 attributes and 308-1423 rows (play-ers). 


Finally, we calculated the importance of all numerical attributes relative to the target attribute (CapHit). 
For this purpose, we used the univariate attribute selection that selecting the best attributes based on univariate statistical tests.
The calculation uses the SelectorKBest class, which determines the number of best attributes in com-bination with suitable statistical test. We have applied this process to two basic types of data for a set of all players and a set of all goalies without a split. 

And the results were:

•	Top 5 goalies attributes: Wt (weight), HT (height), PPSA (power play shots against), GAA (goals against average), SHSA (shorthanded shot against).

•	Top 5 players attributes: Wt (weight), HT (height), TOI/G (time on ice per game), Shift/G (shifts per game), TOI (time on ice). 

Also, we applied the Sequential Forward Selection to identify the most im-portant attributes. 
Sequential Feature Selector algorithms are a family of greedy search algorithms. 
These algorithms add or remove one attribute at the time based on the classifier performance until a variables subset of the desired size is reached. We obtained the following results:

•	Top 16 goalies attributes: GS, OT, GR, MIN, SO, StMIN, StSV%, StGAA, QS, ReMIN, SHSV%, PPSV%, SOW, SOL, SSA and, SGA (the prediction accuracy only 54%, but the best from the all related experiments).

•	Top 8 players attributes: HT, Wt, TOI/G, A/G, PIM/G, Shifts/G, Diff/G and Bl/G (the prediction accuracy 67%).

The results were in some cases the same, but most of the selected attributes were different. 
Attributes selected by SFS algorithm were more trusted.

Modeling and Evaluation

We used the preprocessed data as an input to calculate the models within the polynomial regression method. 
First, we calculated the anticipated CapHit for all goalkeeper and all players without a split. 
For the category of all goalies, the model's precision exceeded 95%, which is a perfect result. 
But for all players, it was only about 54%, which is too low. 
Also, we used polynomial regression to calculate the expected salary for all divided tables

Table	        Score

GoaliesN	    0.84798	

GoaliesU	    0.79729	

GoaliesR	    0.84776	

DefensemanN	    0.54302	

DefensemanU	    0.53995	

DefensemanR	    0.92464

ForwardN	    0.41503

ForwardU	    0.82917

ForwardR	    0.71461

Goalies	        0.95469

Forward	        0.54339

As we can see from the table, for all three goalie categories, we were less accurate than the total set of all goalies. 
But in three cases the players were more precision than all the players, and the other three were not the best. 
Especially in the case of the rookie, we have no very suitable models.
