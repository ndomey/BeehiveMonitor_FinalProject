import Header from "../components/Header";

export default function BeeMonitor() {

    const options = {
      chart: {
        type: 'spline'
      },
      credits: {
        enabled: false,
      },
      data: {
        enablePolling: true,
        dataRefreshRate: 2,
      },
      yAxis: {
        title: {
          text: 'Number of bees'
        }
      },
      xAxis: {
        title: {
          text: 'Time'
        }
      },
      title: false,
      tooltip: {
        borderRadius: 20,
      },
      colors: ['#E9B44C']
    };
  
    fetch('data_log.csv')
      .then(res => {
        return res.text();
    })
    .then(csv => {
      options.data = {
        csv
      };
      Highcharts.chart('container', options)
    })

    return (
        <>
          <Header/>
            <h2>Bee Monitor Chart</h2>
              <div id="container"></div>
        </>
    )
}