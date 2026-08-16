import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Interior Design and Architecture Planner",
    layout="wide"
)

df = pd.read_csv("interior_design_dataset.csv")


def inr(value):
    return f"Rs. {value:,.0f}"


st.sidebar.title("Design Planner")
st.sidebar.write("Interior Designing and Architecture")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Design Planner", "Dataset Explorer", "Analytics"]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "This application demonstrates Streamlit widgets, "
    "user interaction, calculations, dataset filtering "
    "and data visualization."
)


if page == "Home":

    st.title("Interior Design and Architecture Planner")

    st.subheader(
        "Plan, estimate and analyse your interior design project"
    )

    st.write(
        "This application helps users plan an interior design project, "
        "estimate project costs and analyse sample architecture projects."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Projects in Dataset",
            len(df)
        )

    with col2:
        st.metric(
            "Design Styles",
            df["Architecture_Style"].nunique()
        )

    with col3:
        st.metric(
            "Room Types",
            df["Room_Type"].nunique()
        )

    st.markdown("---")

    st.header("Application Features")

    c1, c2 = st.columns(2)

    with c1:
        st.write("Design Planner")
        st.write(
            "Select room type, architectural style, materials, "
            "room dimensions and budget."
        )
        st.write(
            "The application calculates room area and estimated cost."
        )

    with c2:
        st.write("Dataset and Analytics")
        st.write(
            "Explore and filter interior design projects "
            "using different criteria."
        )
        st.write(
            "View charts showing project costs, styles and room areas."
        )

    st.markdown("---")

    st.caption(
        "Python Lab Project | Interior Designing and Architecture"
    )


elif page == "Design Planner":

    st.title("Interior Design Project Planner")

    st.write(
        "Enter the project details to calculate area and estimate cost."
    )

    col1, col2 = st.columns(2)

    with col1:

        project_name = st.text_input(
            "Project Name",
            "My Dream Home"
        )

        room_type = st.selectbox(
            "Select Room Type",
            [
                "Living Room",
                "Bedroom",
                "Kitchen",
                "Bathroom",
                "Dining Room",
                "Home Office"
            ]
        )

        style = st.selectbox(
            "Select Architecture / Interior Style",
            [
                "Modern",
                "Minimalist",
                "Contemporary",
                "Traditional",
                "Industrial",
                "Scandinavian"
            ]
        )

        material = st.multiselect(
            "Preferred Materials",
            [
                "Teak Wood",
                "Oak Wood",
                "MDF",
                "Marble",
                "Granite",
                "Laminate",
                "Glass",
                "Metal"
            ],
            default=["Oak Wood"]
        )

    with col2:

        length = st.number_input(
            "Room Length (feet)",
            min_value=5.0,
            max_value=100.0,
            value=20.0,
            step=1.0
        )

        width = st.number_input(
            "Room Width (feet)",
            min_value=5.0,
            max_value=100.0,
            value=15.0,
            step=1.0
        )

        budget = st.slider(
            "Budget (Rs.)",
            min_value=50000,
            max_value=1000000,
            value=250000,
            step=25000
        )

        priority = st.radio(
            "Design Priority",
            [
                "Aesthetics",
                "Functionality",
                "Budget Efficiency"
            ]
        )

    area = length * width

    rates = {
        "Living Room": 950,
        "Bedroom": 800,
        "Kitchen": 1200,
        "Bathroom": 1000,
        "Dining Room": 750,
        "Home Office": 700
    }

    style_multiplier = {
        "Modern": 1.10,
        "Minimalist": 0.90,
        "Contemporary": 1.15,
        "Traditional": 1.20,
        "Industrial": 1.00,
        "Scandinavian": 1.05
    }

    base_rate = rates[room_type]

    material_multiplier = 1 + (0.05 * len(material))

    estimated_cost = (
        area
        * base_rate
        * style_multiplier[style]
        * material_multiplier
    )

    st.markdown("---")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "Room Area",
            f"{area:,.0f} sq ft"
        )

    with m2:
        st.metric(
            "Estimated Cost",
            inr(estimated_cost)
        )

    with m3:
        difference = budget - estimated_cost

        st.metric(
            "Budget Difference",
            inr(difference)
        )

    if estimated_cost <= budget:
        st.success(
            "The estimated project cost is within your selected budget."
        )
    else:
        st.warning(
            "The estimated project cost exceeds your selected budget."
        )

    st.markdown("---")

    if st.button(
        "Generate Design Recommendation"
    ):

        st.subheader(
            f"Recommendation for {project_name}"
        )

        recommendations = {
            "Modern":
                "Use clean lines, neutral colours, glass, "
                "metal and modular furniture.",

            "Minimalist":
                "Focus on simplicity, open space, "
                "functional furniture and limited decoration.",

            "Contemporary":
                "Combine modern materials, statement lighting "
                "and comfortable furniture.",

            "Traditional":
                "Consider wooden furniture, warm colours, "
                "detailed patterns and classic elements.",

            "Industrial":
                "Use exposed textures, metal elements, "
                "concrete finishes and functional lighting.",

            "Scandinavian":
                "Use light colours, natural wood, soft textures "
                "and simple functional furniture."
        }

        st.info(
            recommendations[style]
        )

        if priority == "Aesthetics":
            st.write(
                "Focus: premium finishes, lighting, furniture "
                "and visual balance."
            )

        elif priority == "Functionality":
            st.write(
                "Focus: storage, movement space, furniture "
                "placement and usability."
            )

        else:
            st.write(
                "Focus: durable materials, essential furniture "
                "and cost-effective finishes."
            )

        if material:
            st.write(
                "Selected materials: "
                + ", ".join(material)
            )
        else:
            st.write(
                "Selected materials: No specific material selected."
            )


elif page == "Dataset Explorer":

    st.title("Interior Design Dataset Explorer")

    st.write(
        "Filter and explore sample interior design projects."
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        selected_rooms = st.multiselect(
            "Room Type",
            sorted(df["Room_Type"].unique()),
            default=sorted(df["Room_Type"].unique())
        )

    with c2:

        selected_styles = st.multiselect(
            "Architecture Style",
            sorted(df["Architecture_Style"].unique()),
            default=sorted(df["Architecture_Style"].unique())
        )

    with c3:

        selected_cities = st.multiselect(
            "City",
            sorted(df["City"].unique()),
            default=sorted(df["City"].unique())
        )

    filtered = df[
        df["Room_Type"].isin(selected_rooms)
        & df["Architecture_Style"].isin(selected_styles)
        & df["City"].isin(selected_cities)
    ]

    st.metric(
        "Filtered Projects",
        len(filtered)
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )


elif page == "Analytics":

    st.title("Interior Design Analytics")

    st.write(
        "Analyse project costs, architecture styles and room areas."
    )

    avg_cost = df["Total_Cost_INR"].mean()
    avg_area = df["Area_sqft"].mean()
    total_budget = df["Budget_INR"].sum()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Average Project Cost",
            inr(avg_cost)
        )

    with c2:
        st.metric(
            "Average Room Area",
            f"{avg_area:,.0f} sq ft"
        )

    with c3:
        st.metric(
            "Total Planned Budget",
            inr(total_budget)
        )

    st.markdown("---")

    st.subheader("Average Project Cost by Room Type")

    room_cost = (
        df.groupby("Room_Type")["Total_Cost_INR"]
        .mean()
        .sort_values(ascending=False)
    )

    fig1, ax1 = plt.subplots()

    ax1.bar(
        room_cost.index,
        room_cost.values
    )

    ax1.set_xlabel("Room Type")
    ax1.set_ylabel("Average Cost (Rs.)")
    ax1.set_title("Average Project Cost by Room Type")

    plt.xticks(rotation=45)

    st.pyplot(fig1)

    st.markdown("---")

    st.subheader("Projects by Architecture Style")

    style_count = df["Architecture_Style"].value_counts()

    fig2, ax2 = plt.subplots()

    ax2.pie(
        style_count.values,
        labels=style_count.index,
        autopct="%1.1f%%"
    )

    ax2.set_title("Projects by Architecture Style")

    st.pyplot(fig2)

    st.markdown("---")

    st.subheader("Room Area vs Project Cost")

    fig3, ax3 = plt.subplots()

    ax3.scatter(
        df["Area_sqft"],
        df["Total_Cost_INR"]
    )

    ax3.set_xlabel("Area (sq ft)")
    ax3.set_ylabel("Total Cost (Rs.)")
    ax3.set_title("Room Area vs Project Cost")

    st.pyplot(fig3)

    st.markdown("---")

    st.subheader("Average Cost by Design Component")

    components = pd.DataFrame(
        {
            "Component": [
                "Furniture",
                "Lighting",
                "Flooring",
                "Paint"
            ],
            "Average_Cost": [
                df["Furniture_Cost_INR"].mean(),
                df["Lighting_Cost_INR"].mean(),
                df["Flooring_Cost_INR"].mean(),
                df["Paint_Cost_INR"].mean()
            ]
        }
    )

    fig4, ax4 = plt.subplots()

    ax4.bar(
        components["Component"],
        components["Average_Cost"]
    )

    ax4.set_xlabel("Design Component")
    ax4.set_ylabel("Average Cost (Rs.)")
    ax4.set_title("Average Cost by Design Component")

    st.pyplot(fig4)

st.markdown("---")

st.caption(
    "Interior Design and Architecture Planner | Streamlit Python Lab"
)