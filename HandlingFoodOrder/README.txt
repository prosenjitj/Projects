CSS Challenge
========================

Project setup :
1. Go to /Root Directory
2. Run and build
    python3 setup.py build

3.Install -
    python3 setup.py install

4. Run the application

    python3 src/main.py \
            -m /<PATH>/items.json \
            -o /<PATH>/orders.json \
            -t /<PATH>/temp \
            -num 10

      items.json : Holding menu and time to prepare Data
      orders.json : Order Details.Big file and actual stream data sources
      temp : Temporary memory folder for persist CART data in Server
      NUM : Number of parallel process, which will help to scale the parallel process.

5. For Data Testing :
python3 tests/test_data.py

For Functional Testing :
python3 tests/test_functional.py

---------------

Backend Log :

#Order Id		Customer Name		Service Name 		Cost		Wait Time
------------------------------------------------------------------------------------------------------------------------------------------------------
1556536013832  	  Monica Martin  		  ClubNub 		 3400 		 408
1556536013835  	  Samantha Reed  		  SuperEats 		 5000 		 804
1556536013838  	  Taylor Perry  		  SuperEats 		 3000 		 624
1556536013840  	  Destiny Cook  		  Mostplates 		 2100 		 252
1556536013841  	  Leah Brooks  		  SuperEats 		 2000 		 264
1556536013843  	  Tyler Cox  		  Mostplates 		 3600 		 300
1556536013844  	  Lindsey Barnes  		  SuperEats 		 600 		 72
1556536013846  	  April Sanders  		  Mostplates 		 5150 		 516
1556536013847  	  Corey Murphy  		  SuperEats 		 5000 		 624
1556536013849  	  Anthony Anderson  		  SuperEats 		 950 		 120
1556536013850  	  Destiny Richardson  		  Mostplates 		 2400 		 288




#Thread Id	#Order Id	 Priority		Item(Same Orders)			Quantity	Wait Time	Service Name
------------------------------------------------------------------------------------------------------------------------------------------------------
0 --> CART:  1556536013832	1	Puff Pastry Chicken Potpie			1	780	ClubNub
1 --> CART:  1556536013832	1	Blue Cheese-Crusted Sirloin Steaks			1	660	ClubNub
2 --> CART:  1556536013832	1	The Ultimate Chicken Noodle Soup			1	600	ClubNub
3 --> CART:  1556536013835	2	Saucy Chicken Thighs			1	420	SuperEats
4 --> CART:  1556536013835	2	Chicken and Wild Rice Bake			1	300	SuperEats
0 --> CART:  1556536013835	2	Easy Chicken Cordon Bleu			5	540	SuperEats
1 --> CART:  1556536013835	2	Easy Chicken Cordon Bleu			5	540	SuperEats
2 --> CART:  1556536013835	2	Easy Chicken Cordon Bleu			5	540	SuperEats
3 --> CART:  1556536013835	2	Easy Chicken Cordon Bleu			5	540	SuperEats
4 --> CART:  1556536013835	2	Easy Chicken Cordon Bleu			5	540	SuperEats
0 --> CART:  1556536013835	2	Honey Chipotle Ribs			1	600	SuperEats
2 --> CART:  1556536013838	3	Mom's Meat Loaf			2	900	SuperEats
1 --> CART:  1556536013838	3	Mom's Meat Loaf			2	900	SuperEats
3 --> CART:  1556536013838	3	Big John's Chili-Rubbed Ribs			2	660	SuperEats
4 --> CART:  1556536013838	3	Big John's Chili-Rubbed Ribs			2	660	SuperEats
0 --> CART:  1556536013840	4	Au Gratin Peas and Potatoes			3	420	Mostplates
1 --> CART:  1556536013840	4	Au Gratin Peas and Potatoes			3	420	Mostplates


# Thread Id : Seq of parallel processes
Priority : Order by data present in Orders.json


Business Usecases :
Path : /root/ReportForService_Cost.png
- Report based on Service Cost

Path : /root/ReportBasedonGroupByServiceCost.png
- Report Based on GroupBy Service Cost

Path : /root/ReportBasedOnWaititime.png
- Report Based on Wait Time



Details on Process :

Components :

Multi-Directional Carts  : More analytical Variable will be stored in Single CART object, Which help for further calculation.
                           Calculated field already stored and can able to persist in server for later used.
Data Frame : Data stored in Table structure. It will help to query on top of data. Like, GroupBy, Sum.
             It has inbuild function. Huge data can be cached


Advantage of choosing Technologies :

Python – Light weight and can handle Huge Data. Transformation is easy.
Multithreading – Process Orders in Parallel
    Note : Why not Multiprocessing - Mutiprocess also can make it faster for Muticore Servers. But, Multithreading is preferable for local machine.

Deque – Queue to store data and maintain the seq. It is Thread Safe and sequencial access at Data PipeLine flow.
Pandas – Famous for In-memory cache for huge data. Data can be queried and Bring report is easy.
matplotlib - Data Visualisation. Data can be reprsented in all different charts. We preferred Bar chart for this project.
pickle - Help to persist data in local and make Object transparent to process at the time of reading.


Features :
Scaling : Increse of number of process , it can be scaled to process in less time
Persist : Muti Directional Calculated data will stored in local. Whenever report is required , based on OrderId , we can build statistics.
In - Memory Cache : Pandas can handle in-mory cache for Huge Dataset



