// Code goes here
var ctx = document.getElementById("chart").getContext("2d");
new Chart(ctx, {
  type: "line",
  data: {
    labels: ["Visit 1", "Visit 2", "Visit 3", "Visit 4", "Visit 5"],
    datasets: [
      {
        label: "LVEF % (Echo)",
        yAxisID: "A",
        borderColor: "#ffbaa2",
        backgroundColor: "white",
        data: [80, 70, 30, 20, 35],
        fill: false,
      },
      {
        label: "Rhythm",
        yAxisID: "B",
        borderColor: "#91cf96",
        backgroundColor: "white",
        data: [80, 76, 79, 82, 80],
        fill: false,
      },
      {
        label: "Height",
        yAxisID: "C",
        borderColor: "#c881d2",
        backgroundColor: "white",
        data: [185, 184, 183, 184, 185],
        fill: false,
      },
      {
        label: "Weight",
        yAxisID: "D",
        borderColor: "#29b6f6",
        backgroundColor: "white",
        data: [65, 65, 65, 65, 65],
        fill: false,
      },
    ],
  },
  options: {
    tooltips: {
      mode: "nearest",
    },
    scales: {
      yAxes: [
        {
          id: "A",
          type: "linear",
          position: "left",
          ticks: {
            min: 0,
            max: 100,
            stepSize: 10,
            fontColor: "#ffbaa2",
            callback: function (value, index, values) {
              return value + " %";
            },
          },
        },
        {
          id: "B",
          type: "linear",
          position: "right",
          ticks: {
            min: 60,
            max: 140,
            stepSize: 16,
            fontColor: "#91cf96",
            callback: function (value, index, values) {
              return value + " bpm";
            },
          },
        },
        {
          id: "C",
          type: "linear",
          position: "right",
          ticks: {
            min: 160,
            max: 190,
            stepSize: 6,
            fontColor: "#c881d2",
            callback: function (value, index, values) {
              return value + " cm";
            },
          },
        },
        {
          id: "D",
          type: "linear",
          position: "right",
          ticks: {
            min: 50,
            max: 100,
            stepSize: 10,
            fontColor: "#29b6f6",
            callback: function (value, index, values) {
              return value + " kg";
            },
          },
          scaleLabel: {
            display: false,
          },
        },
      ],
    },
    elements: {
      line: {
        tension: 0, // disables bezier curves
      },
      point: {
        radius: 4,
        borderWidth: 2,
        pointStyle: "circle",
      },
    },
  },
});
