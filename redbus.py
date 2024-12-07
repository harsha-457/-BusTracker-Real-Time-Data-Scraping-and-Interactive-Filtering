import pandas as pd
import mysql.connector
import streamlit as st 
from streamlit_option_menu import option_menu  #used for selecting an option from list of options in a menu
import plotly.express as px 
import plotly.graph_objects as go
from tabulate import tabulate
import altair as alt

#each bus we have to filter
#now we have to take route_name from each dataframe and then append to list

#andhra bus
andhra=[]
df_a=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\andhra_bus.csv")
for i,r in df_a.iterrows():  #traverse through each row
    andhra.append(r['Route_name'])   # add that row in new list


#Assam bus
assam=[]
df_am=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\assam_bus.csv")
for i,r in df_am.iterrows():
    assam.append(r['Route_name'])

#bihar bus
bihar=[]
df_b=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\bihar_bus.csv")
for i,r in df_b.iterrows():
    bihar.append(r['Route_name'])


#goa bus
goa=[]
df_g=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\goa.csv")
for i,r in df_g.iterrows():
    goa.append(r['Route_name'])
    
#gujurat
gujurat=[]
df_gt=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\gujurat_bus.csv")
for i,r in df_gt.iterrows():
    gujurat.append(r['Route_name'])

#himachal
himachal=[]
df_h=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\himachal_bus.csv")
for i,r in df_h.iterrows():
    himachal.append(r['Route_name'])

#kerala 
kerala=[]
df_k=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\kerala_bus.csv")
for i,r in df_k.iterrows():
    kerala.append(r["Route_name"])

#ksm bus
ksm_roadways=[]
df_ksm=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\ksmroadways_bus.csv")
for i,r in df_ksm.iterrows():
    ksm_roadways.append(r['Route_name'])
    
#meghalaya
meghalaya=[]
df_m=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\meghalaya_bus.csv")
for i,r in df_m.iterrows():
    meghalaya.append(r["Route_name"])
    
#psr bus
psr=[]
df_psr=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\psr_travels_bus.csv")
for i,r in df_psr.iterrows():
    psr.append(r['Route_name'])

#rajasthan
rajasthan=[]
df_r=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\rajasthan_bus.csv")
for i,r in df_r.iterrows():
    rajasthan.append(r['Route_name'])

#royal_rich
royal_rich=[]
df_rr=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\royal_rich_bus.csv")
for i,r in df_rr.iterrows():
    royal_rich.append(r['Route_name'])

#telangana
telangana=[]
df_t=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\telangana_bus.csv")
for i,r in df_t.iterrows():
    telangana.append(r['Route_name'])

#uttar_pradesh
uttar_pradesh=[]
df_up=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\uttar_bus.csv")
for i,r in df_up.iterrows():
    uttar_pradesh.append(r['Route_name'])

#west_bengal
west_bengal=[]
df_wb=pd.read_csv("C:\\Users\\Harsha\\Desktop\\guvi\\code\\PROJECT\\west_bengal_bus.csv")
for i,r in df_wb.iterrows():
    west_bengal.append(r['Route_name'])

###############################################

# ---------------> STREAMLIT PART ------------>

###############################################



#setting streamlit page
st.set_page_config(layout="wide",page_icon=":material/directions_bus:",page_title="RedBus Project",initial_sidebar_state="expanded")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://media.istockphoto.com/id/1045929296/photo/trafficlights-in-the-city-at-night-time.jpg");
        background-size: cover; /* Ensures the image covers the entire container */
        background-position: center; /* Centers the image */
        background-repeat: no-repeat; /* Prevents the image from repeating */
        background-attachment: fixed; /* Fixes the image in place when scrolling */
        height: 100vh; /* Sets the height to 100% of the viewport height */
        width: 100vw; /* Sets the width to 100% of the viewport width */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background-color: #60191900; /* Replace with your desired color */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Ensure font size does not change on hover */
    .nav-link {
        font-size: 18px !important;
    }
    .nav-link:hover {
        font-size: 18px !important;
        color: #32789e !important; /* Change only the color on hover */
    }
    .nav-link-selected {
        font-size: 20px !important;
    }
    </style>
    """,unsafe_allow_html=True
)




# Theme button in the sidebar



with st.sidebar:
    #THEME CONTROL  OPERATIONAL IN SIDEBAR
    
    
    menu = option_menu(
        "Main Menu", 
        ["Home", 'Bus Routes'], 
        icons=['house', 'map'], 
        menu_icon="cast", 
        default_index=0,
        styles={
            "icon":{"font-size":"21px"},
            # "nav-link-selected": {"background-color": "#0b0bdd","font-size":"20px"}
        }
    )


if menu=="Home":
    st.title(":red[:material/analytics:] :red[🚌BusTracker: Real-Time Data Scraping and Interactive Filtering]")
    st.text("")
    st.subheader(" ")
    st.markdown(""" ### :violet[:material/tooltip:] :red[*Objective*]

                 BusTracker is an advanced data scraping and visualization tool that automates the collection of real-time bus travel data from the RedBus platform. This project leverages      Selenium for web scraping, extracting detailed information such as bus routes, schedules, prices, and seat availability. The data is then structured into a SQL database and visualized through an interactive Streamlit application, allowing dynamic filtering and analysis. 

    """)
    st.markdown("---")

    # Why BusTracker Section
    st.markdown(
        """
        ## 🌟 *Why BusTracker?*
        *BusTracker* combines advanced data scraping techniques with a user-friendly visualization platform, 
        empowering businesses and individuals to make informed decisions based on real-time travel data.
        """
    )
    st.success("Get started with BusTracker today!")

    dfbus=pd.read_csv("C:\\Redbus\\dfbus.csv")
    
    fig = px.scatter(dfbus, 
                 x='Price', 
                 y='Ratings', 
                 color='Bus_type',
                 size='Seats_Available',
                 hover_name='Bus_name',
                 title='Bus Price vs Ratings',
                 labels={'Price': 'Ticket Price', 'Ratings': 'Bus Ratings'})

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    labels = dfbus['Seats_Available']
    values = dfbus['Ratings']

    # Create the Pie chart
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.1)])
    fig2.update_layout(
        title_text="distribution",
        title_x=0.45
    )
    st.plotly_chart(fig2)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    
    
    dfbus = pd.read_csv("C:\\Redbus\\dfbus.csv")

    # Create an Altair chart
    chart = alt.Chart(dfbus).mark_circle().encode(
        y='Price:Q',               # 'Price' as a quantitative (float) field
        x='Total_duration:N',      # 'total_duration' as a nominal (string) field
        color='Route_name:N',          # Adjust this to the appropriate categorical column in your data
    ).interactive()

        # Display the chart
    st.altair_chart(chart,use_container_width=True)
        
    #altair
    # Top panel is a scatter plot of Total_duration vs Price
    brush = alt.selection_interval(encodings=['x'])

# Define the click selection for interactivity
    click = alt.selection_single(encodings=['y'])

    # Top panel is a scatter plot of Total_duration vs Price
    points = (
        alt.Chart(dfbus)
        .mark_point()
        .encode(
            alt.X("Total_duration:N", title="Total Duration"),
            alt.Y("Price:Q", title="Price"),
            color=alt.condition(brush, "Bus_type:N", alt.value("lightgray")),
            size=alt.Size("Price:Q", scale=alt.Scale(range=[5, 200])),
        )
        .properties(width=550, height=300)
        .add_selection(brush)
        .transform_filter(click)
    )

    # Bottom panel is a bar chart of Bus_type
    bars = (
        alt.Chart(dfbus)
        .mark_bar()
        .encode(
            y="Bus_type:N",
            x="count():Q",
            color=alt.condition(click, alt.Color('Bus_type:N', legend=None), alt.value("lightgray")),
        )
        .transform_filter(brush)
        .properties(width=300, height=700)
        .add_selection(click)
    )
        # Combine the charts
    chart = alt.vconcat(points, bars, title="Bus Data Analysis")

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)
    
    
if menu=="Bus Routes":
    
    st.title(":green[:material/filter_alt:]    :blue[Dynamic Filtering of Data]")
    
    
    col1,col2=st.columns(2)
    with col1:
        state=st.selectbox("List of States",["andhra", "assam", "bihar", "goa", "gujurat", "himachal","kerala","ksm_roadways","meghalaya",
                                          "psr", "rajasthan", "royal_rich", "telangana","uttar_pradesh", "west_bengal"])
    with col2:
        select_type=st.selectbox("choose bus type",["A/C","NON A/C","sleeper","semi-sleeper","seater","others"])
    with col1:
        fare = st.number_input("Enter fare", min_value=40, max_value=5000, value=40, step=50)
        #select_fare = st.number_input("Enter bus fare", min_value=40, max_value=5000, value=40, step=1)
    with col2:
        select_rating = st.slider("Choose rating", min_value=1, max_value=5, value=5, step=1)
    with col1:
        TIME=st.time_input("select the time")  
    #time_str=TIME.strftime("%H:%M:%S")  


    
    #ANDHRA BUS FILTERATION
    if state=="andhra":
        with col2:
            k=st.selectbox("List of routes",andhra)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #ASSAM
    if state=="assam":
        with col2:
            k=st.selectbox("List of routes",assam)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out2=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out2,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result2 = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result2,use_container_width=True)
        
    #BIHAR
    
    if state=="bihar":
        with col2:
            k=st.selectbox("List of routes",bihar)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out2=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out2,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result2 = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result2,use_container_width=True)
    
    #GOA
    
    if state=="goa":
        with col2:
           k=st.selectbox("List of routes",goa)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
        
        #GUJURAT
    
    if state=="gujurat":
        with col2:
           k=st.selectbox("List of routes",gujurat)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #HIMACHAL
    if state=="himachal":
        with col2:
           k=st.selectbox("List of routes",himachal)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
        
        #KERALA
        
    if state=="kerala":
        with col2:  
          k=st.selectbox("List of routes",kerala)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #KSM_ROADWAYS
    if state=="ksm_roadways":
        with col2:
           k=st.selectbox("List of routes",ksm_roadways)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #MEGHALAYA
    if state=="meghalya":
        with col2:
           k=st.selectbox("List of routes",meghalaya)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
    #PSR
    if state=="psr":
        with col2:   
           k=st.selectbox("List of routes",psr)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    
    #RAJASTHAN
    if state=="rajasthan":
        with col2:
           k=st.selectbox("List of routes",rajasthan)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)

    #ROYAL_RICH
    if state=="royal_rich":
        with col2:   
           k=st.selectbox("List of routes",royal_rich)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                 bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)

    #TELANGANA
    if state=="telangana":
        with col2:   
           k=st.selectbox("List of routes",telangana)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                 bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)

    #UTTAR_PRADESH
    if state=="uttar_pradesh":
        with col2:   
           k=st.selectbox("List of routes",uttar_pradesh)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                 bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)

    #WEST_BENGAL
    if state=="west_bengal":
        with col2:   
           k=st.selectbox("List of routes",west_bengal)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="project",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                 bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM Redbus
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND departing_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and departing_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)