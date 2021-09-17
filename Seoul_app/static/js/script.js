var canvas = document.getElementById("test1").getContext("2d");
new Chart(canvas, {
  type: "line",
  data: {
    labels: [
      "Morning 6am-12pm",
      "Afternoon 12pm-4pm",
      "Evening 4pm-7pm",
      "Night 7pm-12am",
      "Dawn 12am-6am",
    ],
    datasets: [
      {
        label: "Temperature",
        yAxisID: "A",
        data: [30, 32, 33, 31, 30],
      },
      {
        label: "Humidity",
        yAxisID: "B",
        data: [80, 77, 74, 79, 83],
        lineTension: 0.3,
        fill: false,
        borderColor: "lightblue",
        backgroundColor: "transparent",
        pointBorderColor: "lightblue",
        pointBackgroundColor: "lightgreen",
        pointRadius: 5,
        pointHoverRadius: 15,
        pointHitRadius: 30,
        pointBorderWidth: 2,
      },
    ],
  },
  options: {
    responsive: false,
    scales: {
      yAxes: [
        {
          id: "A",
          type: "linear",
          position: "left",
        },
        {
          id: "B",
          type: "linear",
          position: "right",
          ticks: {
            max: 100,
            min: 0,
          },
        },
      ],
    },
    annotation: {
      annotations: [
        {
          type: "line",
          mode: "horizontal",
          scaleID: "A",
          value: 32,
          borderColor: "rgb(75, 0, 0)",
          borderWidth: 4,
          label: {
            enabled: false,
            content: "Test label",
          },
        },
      ],
    },
  },
});

var canvas = document.getElementById("test2").getContext("2d");
new Chart(canvas, {
  type: "line",
  data: {
    labels: [
      "Morning 6am-12pm",
      "Afternoon 12pm-4pm",
      "Evening 4pm-7pm",
      "Night 7pm-12am",
      "Dawn 12am-6am",
    ],
    datasets: [
      {
        label: "Temperature",
        yAxisID: "A",
        data: [30, 32, 33, 31, 30],
      },
      {
        label: "Humidity",
        yAxisID: "B",
        data: [80, 77, 74, 79, 83],
        lineTension: 0.3,
        fill: false,
        borderColor: "lightblue",
        backgroundColor: "transparent",
        pointBorderColor: "lightblue",
        pointBackgroundColor: "lightgreen",
        pointRadius: 5,
        pointHoverRadius: 15,
        pointHitRadius: 30,
        pointBorderWidth: 2,
      },
    ],
  },
  options: {
    responsive: false,
    scales: {
      yAxes: [
        {
          id: "A",
          type: "linear",
          position: "left",
          ticks: {
            min: 0,
            max: 50,
          },
        },
        {
          id: "B",
          type: "linear",
          position: "right",
          ticks: {
            min: 0,
            max: 100,
          },
        },
      ],
    },
    annotation: {
      annotations: [
        {
          type: "line",
          mode: "horizontal",
          scaleID: "A",
          value: 32,
          borderColor: "rgb(75, 0, 0)",
          borderWidth: 4,
          label: {
            enabled: false,
            content: "Test label",
          },
        },
      ],
    },
  },
});
