import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy
#Lewis Francis C1826277
brainGroup = pd.read_excel(r'dfBrainGroup.xlsx')
leukemiaGroup = pd.read_excel(r'LeukemiaGroup.xlsx')
lymphomaGroup = pd.read_excel(r'LymphomaGroup.xlsx')
melanomaGroup = pd.read_excel(r'MelanomaGroup.xlsx')
thyroidGroup = pd.read_excel(r'ThyroidGroup.xlsx')

#Need to fix some pre processing stuff, need to make sure they're all the same size age ranges so just do that

yBrain = [brainGroup["1-Year Survival (%)"],brainGroup["2-Year Survival (%)"],brainGroup["3-Year Survival (%)"],brainGroup["4-Year Survival (%)"],brainGroup["5-Year Survival (%)"]]





fig = px.bar(brainGroup,x = brainGroup["Age At Diagnosis"],y = yBrain , title="Cancer type survival percentage based on years with cancer",
             labels={
                     "value": "Survival (%)",
                     "index": "Age brackets",
                     "variable": "Years"
                 })

fig.update_layout(
    barmode='group',
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            x=0.7,
            y=1.2,
            showactive=True,
            buttons=list(
                [
                    dict(
                        label="Brain Cancer",
                        method="update",
                        args=[{"y": [brainGroup["1-Year Survival (%)"],brainGroup["2-Year Survival (%)"],brainGroup["3-Year Survival (%)"],brainGroup["4-Year Survival (%)"],brainGroup["5-Year Survival (%)"]]}]
                    ),
                    dict(
                        label="Leukemia",
                        method="update",
                        args=[{"y": [leukemiaGroup["1-Year Survival (%)"],leukemiaGroup["2-Year Survival (%)"],leukemiaGroup["3-Year Survival (%)"],leukemiaGroup["4-Year Survival (%)"],leukemiaGroup["5-Year Survival (%)"]]}]
                    ),
                    dict(
                        label="Lymphoma",
                        method="update",
                        args=[{"y": [lymphomaGroup["1-Year Survival (%)"],lymphomaGroup["2-Year Survival (%)"],lymphomaGroup["3-Year Survival (%)"],lymphomaGroup["4-Year Survival (%)"],lymphomaGroup["5-Year Survival (%)"]]}]

                    ),
                    dict(
                        label="Melanoma",
                        method="update",
                        args=[{"y": [melanomaGroup["1-Year Survival (%)"],melanomaGroup["2-Year Survival (%)"],melanomaGroup["3-Year Survival (%)"],melanomaGroup["4-Year Survival (%)"],melanomaGroup["5-Year Survival (%)"]]}]
                              
                    ),
                    dict(
                        label="Thyroid",
                        method="update",
                        args=[{"y": [thyroidGroup["1-Year Survival (%)"],thyroidGroup["2-Year Survival (%)"],thyroidGroup["3-Year Survival (%)"],thyroidGroup["4-Year Survival (%)"],thyroidGroup["5-Year Survival (%)"]]}]
                    )
                    ]))])
fig.show()
