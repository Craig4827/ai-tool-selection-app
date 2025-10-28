
import streamlit as st

# Embedded data from Excel (simplified example)
types_vs_purpose = {
    "Product Development": {
        "Detail Design": ["Creative/Design AI", "Code Generation AI", "Simulation & Digital Twin AI"],
        "Conceptualization": ["Text Generation AI", "Image Generation AI"]
    },
    "Marketing": {
        "Content Creation": ["Text Generation AI", "Image Generation AI"],
        "Campaign Execution": ["Conversational AI / Chatbots"]
    }
}

tools_vs_types = [
    {"Tool": "Figma AI", "Type": "Creative/Design AI", "Features": "Design, prototyping", "Pricing": "Freemium", "Link": "https://www.figma.com/ai/"},
    {"Tool": "Canva AI", "Type": "Creative/Design AI", "Features": "Graphic design", "Pricing": "Freemium", "Link": "https://www.canva.com/ai/"},
    {"Tool": "GitHub Copilot", "Type": "Code Generation AI", "Features": "Code suggestions", "Pricing": "Subscription", "Link": "https://github.com/features/copilot"}
]

st.title("AI Tool Selection Assistant")

# Step 1: Select Business Function & Activity
st.header("Step 1: Select Business Function & Activity")
selected_function = st.selectbox("Business Function", list(types_vs_purpose.keys()))
selected_activity = st.selectbox("Activity", list(types_vs_purpose[selected_function].keys()))

# Step 2: Filter AI Tool Types
tool_types = types_vs_purpose[selected_function][selected_activity]
selected_type = st.selectbox("AI Tool Type", tool_types)

# Step 3: Show Matching Tools
st.header("Step 2: Matching AI Tools")
matching_tools = [tool for tool in tools_vs_types if tool["Type"] == selected_type]

if matching_tools:
    st.write("Matching Tools:")
    for tool in matching_tools:
        st.markdown(f"**{tool['Tool']}** - {tool['Features']} | Pricing: {tool['Pricing']} | [Visit]({tool['Link']})")

    # Step 4: Scoring
    st.header("Step 3: Score Tools")
    scores = {}
    for tool in matching_tools:
        score = st.slider(f"Score {tool['Tool']} (1-5)", 1, 5, 3)
        scores[tool['Tool']] = score

    # Recommendation Logic
    if scores:
        best_tool = max(scores, key=scores.get)
        st.success(f"Recommended Tool: {best_tool}")
        st.write("Implementation Advice:")
        st.write("- Check integration options")
        st.write("- Start with a pilot/test")
        st.write("- Monitor performance and ROI")
else:
    st.warning("No matching tools found for this type.")
