from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Create your views here.
@login_required
def spt(request):
    def scatter():

        fig = make_subplots(rows=1, cols=2, shared_xaxes=True,
                            shared_yaxes=False,)

        x_bar = ['NA', 'Solo']

        y_bar = [
            [0, 3, 5, 8, 10, 13],
            ['Areia','Areia argilosa', 'Areia', 'Areia argilosa', 'Areia siltosa'],
            ['rgba(242,201,76,0.7)', 'rgba(130,130,130,0.7)', 'rgba(242,201,76,0.7)', 'rgba(130,130,130,0.7)', 'rgba(242,153,74,0.7)'],
        ]

        x_prof = [
            'z = 3 m', 'z = 4 m', 'z = 5 m', 'z = 6 m', 'z = 7 m',
            'z = 8 m', 'z = 9 m', 'z = 10 m', 'z = 11 m', 'z = 12 m',
            'z = 13 m', 'z = 14 m', 'z = 15 m', 'z = 16 m',
        ]

        y_spt = [
            41, 37, 35, 31, 33, 31, 22, 25, 19, 11, 15, 6, 4, 0
        ]

        y_spt_i = [
            39, 36, 31, 29, 33, 27, 24, 24, 16, 11, 8, 5, 2, 0
        ]

        # Gráfico de barra
        fig.append_trace(go.Bar(
            x=x_bar,
            y=[9, 0],
            hovertemplate="_",
            name="Nível do LF",
            marker=dict(
                color='rgba(78, 115, 223, 0.7)',
            )), 1, 1),

        for i in range(1, len(y_bar[0])):
            fig.append_trace(go.Bar(
                x=x_bar,
                y=[0, y_bar[0][i]-y_bar[0][i-1]],
                hovertemplate="%{x}",
                name=y_bar[1][i-1],
                marker=dict(
                    color=y_bar[2][i-1],
                )), 1, 1),

        # Gráfico Scatter

        fig.append_trace(go.Scatter(
            x=y_spt, y=x_prof,
            hovertemplate="%{y}<br>NSPT = %{x}</br>",
            name='',
            mode='lines+markers+text',
            line_color='#EB5757',
        ), 1, 2)

        fig.append_trace(go.Scatter(
            x=y_spt_i, y=x_prof,
            hovertemplate="%{y}<br>NSPT_i = %{x}</br>",
            mode='lines+markers+text',
            line_color='rgba(222, 222, 222, 0.7)',
        ), 1, 2)

        # Layout

        fig.update_layout(
            barmode='relative',
            showlegend=False,
            height=1000,
            yaxis=dict(
                ticktext=[
                    'z = 3 m', 'z = 4 m', 'z = 5 m', 'z = 6 m', 'z = 7 m',
                    'z = 8 m', 'z = 9 m', 'z = 10 m', 'z = 11 m', 'z = 12 m',
                    'z = 13 m', 'z = 14 m', 'z = 15 m', 'z = 16 m',
                ],
                tickvals=[
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
                ],
                ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10,
                domain=[0.05, 0.935],
                showgrid=True,
            ),
            yaxis2=dict(
                showline=True,
                linecolor='rgba(82, 82, 82, 0.6)',
                linewidth=3,
                showticklabels=False,
                domain=[0, 0.94],
            ),
            xaxis=dict(
                domain=[0.05, 0.43],
                side='top',
                showgrid=False,
                showticklabels=False,
            ),
            xaxis2=dict(
                domain=[0.47, 1],
                side='top',
                dtick=5,
            ),
            margin=dict(l=100, r=40, t=0, b=50),
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)',
            font=dict(
                size=12,
                color="#828282",
            )
        )

        fig.update_yaxes= range(y_bar[0][0], y_bar[0][len(y_bar)])

        annotations = []

        # Adding labels
        for i in range(1, len(y_bar[0])):
            # labeling the bar soils
            annotations.append(dict(xref='x1', yref='y1',
                                    y=(y_bar[0][i-1]+y_bar[0][i])/2, x=3,
                                    text=str(y_bar[1][i-1]),
                                    font=dict(family='Arial', size=14,
                                              color='#828282'),
                                    showarrow=False))

        for yd, xd in zip(
                    y_spt,
                    x_prof,
        ):
            # labeling the scatter spt
            annotations.append(dict(xref='x2', yref='y2',
                                    y=xd, x=yd + 6,
                                    text='NSPT = ' + str(yd),
                                    font=dict(family='Arial', size=12,
                                                color='#EB5757'),
                                    showarrow=False))

        fig.update_layout(annotations=annotations)

        plot_div = plot(fig, output_type='div', include_plotlyjs=False)

        return plot_div

    context = {
        'plot': scatter()
    }

    return render(request, 'spt.html', context)


# View home
@login_required
def home(request):
    def scatter():
        fig = go.Figure()

        fig.add_trace(go.Carpet(
            a=[4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
            b=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
            y=[11.5, 13, 13.5, 12.5, 14, 14.5, 15, 16, 17, 17.5, 18, 19.5],
            aaxis=dict(
                tickprefix='',
                ticksuffix='',
                smoothing=1,
                minorgridcount=9
            ),
            baxis=dict(
                tickprefix='',
                ticksuffix='',
                smoothing=1,
                minorgridcount=9
            )
        ))

        fig.add_trace(go.Scattercarpet(
            name="SPT 01",
            a=[5],
            b=[2.5],
            hovertemplate="x = %{a}m<br>y = %{b}m</br>z = 16m",
            texttemplate="SPT 01",
            marker=dict(
                size=[20],
                color=["#EB5757"]
            )
        ))

        fig.update_layout(
            height=314,
            margin=dict(l=100, r=20, t=40, b=60),
            showlegend=True,
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)',
            font=dict(
                size=12,
                color="#828282",
            )
        )

        plot_div = plot(fig, output_type='div', include_plotlyjs=False)

        return plot_div

    context = {
        'plot': scatter()
    }

    return render(request, 'home.html', context)