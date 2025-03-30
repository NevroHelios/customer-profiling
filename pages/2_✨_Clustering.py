import streamlit as st
import pandas as pd


with st.sidebar:
    st.markdown("## 🧭 Navigation")
    
    st.markdown("### 📊 K-Means Clustering")
    st.markdown("- [1.1 📈 Determining Optimal K using Elbow Method](#1-1-determining-optimal-k-using-elbow-method)")
    st.markdown("- [1.2 🔍 Validating with Silhouette Score](#1-2-validating-with-silhouette-score)")
    st.markdown("- [1.3 👥 Cluster Profiles](#1-3-cluster-profiles)")
    st.markdown("- [1.4 📈 Response Rate by Cluster](#1-4-response-rate-by-cluster)")
    
    st.markdown("---")  
    
    st.markdown("### 🧩 DBSCAN Clustering")
    st.markdown("- [2.1 ⚙️ Determining Optimal Epsilon](#2-1-determining-optimal-epsilon)")
    st.markdown("- [2.2 📑 DBSCAN Results](#2-2-dbscan-results)")



st.title("Customer Clustering Analysis")

st.header("1. K-Means Clustering")

st.subheader("1.1 Determining Optimal K using Elbow Method")
st.image("charts/elbow_k.png", caption="Elbow Method Plot")
# st.write("Based on the elbow method, we observed that k=2 could be optimal number of clusters.")

st.subheader("1.2 Validating with Silhouette Score")
st.markdown("""
-   For k = 2, the average silhouette_score is: 0.3907429326000891
-   For k = 3, the average silhouette_score is: 0.1840523042271064
-   For k = 4, the average silhouette_score is: 0.19449549683708328
-   For k = 5, the average silhouette_score is: 0.1824770552284108
-   For k = 6, the average silhouette_score is: 0.17642859284502213
-   For k = 7, the average silhouette_score is: 0.205371099133871
""")
st.expander("See the chart").image("charts/silhouette_score.png", caption="Silhouette Score Plot")
st.write("Remarks")
st.markdown("""
-   for `k=2` the silhoutte score is much higher than the rest
-   in elbow method k=6 menain a strong candidate
-   but `magnitude` is the key so we choose `k = 2`
""")


st.subheader("1.3 Cluster Profiles")
st.dataframe(pd.read_csv("data/cluster_profile.csv"))

st.subheader("1.4 Response Rate by Cluster")
st.dataframe(pd.read_csv("data/response_rate.csv"), use_container_width=False)

st.header("2. DBSCAN Clustering")

st.subheader("2.1 Determining Optimal Epsilon")
st.write("Using the k-distance elbow method to find optimal epsilon value")
st.image("charts/elbow_d.png", caption="Epsilon Elbow Method Plot")
st.write("Based on the elbow method, optimal epsilon value was determined to be 2.5")

st.subheader("2.2 DBSCAN Results")
st.write("""
- Number of clusters found: 4
- Number of noise points: 29
""")