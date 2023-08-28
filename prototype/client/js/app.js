function getNewBuildingValue() {
  var uiNewBuilding = document.getElementsByName("uiNewBuilding");
  for(var i in uiNewBuilding) {
    if(uiNewBuilding[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getIsBasementValue() {
  var uiIsBasement = document.getElementsByName("uiIsBasement");
  for(var i in uiIsBasement) {
    if(uiIsBasement[i].checked) {
        return parseInt(i)+1;
    }
  }
    return -1; // Invalid Value
}
  
function getHasBalconyValue() {
  var uiHasBalcony = document.getElementsByName("uiHasBalcony");
  for(var i in uiHasBalcony) {
    if(uiHasBalcony[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getPassengerLiftsCountValue() {
  var uiPassengerLiftsCount = document.getElementsByName("uiPassengerLiftsCount");
  for(var i in uiPassengerLiftsCount) {
    if(uiPassengerLiftsCount[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getCargoLiftsCountValue() {
  var uiCargoLiftsCount = document.getElementsByName("uiCargoLiftsCount");
  for(var i in uiCargoLiftsCount) {
    if(uiCargoLiftsCount[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getIsFirstFloorValue() {
  var uiIsFirstFloor = document.getElementsByName("uiIsFirstFloor");
  for(var i in uiIsFirstFloor) {
    if(uiIsFirstFloor[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getIsLastFloorValue() {
  var uiIsLastFloor = document.getElementsByName("uiIsLastFloor");
  for(var i in uiIsLastFloor) {
    if(uiIsLastFloor[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getIsCompleteValue() {
  var uiIsComplete = document.getElementsByName("uiIsComplete");
  for(var i in uiIsComplete) {
    if(uiIsComplete[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getIsApartmentsValue() {
  var uiIsApartments = document.getElementsByName("uiIsApartments");
  for(var i in uiIsApartments) {
    if(uiIsApartments[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getFromDeveloperValue() {
  var uiFromDeveloper = document.getElementsByName("uiFromDeveloper");
  for(var i in uiFromDeveloper) {
    if(uiFromDeveloper[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getIsAuctionValue() {
  var uiIsAuction = document.getElementsByName("uiIsAuction");
  for(var i in uiIsAuction) {
    if(uiIsAuction[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var newBuilding = getNewBuildingValue();
  var floorNumber = document.getElementById("uiFloorNumber");
  var fromDeveloper = getFromDeveloperValue();
  var isApartments = getIsApartmentsValue();
  var isAuction = getIsAuctionValue();
  var kitchenArea = document.getElementById("uiKitchenArea");
  var livingArea = document.getElementById("uiLivingArea");
  var roomsCount = document.getElementById("uiRoomsCount");
  var totalArea = document.getElementById("uiTotalArea");
  var floorsCount = document.getElementById("uiFloorsCount");
  var isComplete = getIsCompleteValue();
  var passengerLiftsCount = getPassengerLiftsCountValue();
  var cargoLiftsCount = getCargoLiftsCountValue();
  var hasBalcony = getHasBalconyValue();
  var isBasement = getIsBasementValue();
  var isFirstFloor = getIsFirstFloorValue();
  var isLastFloor = getIsLastFloorValue();
  var flatType = document.getElementById("uiFlatType");
  var region = document.getElementById("uiRegion");
  var city = document.getElementById("uiCity");
  var materialType = document.getElementById("uiMaterialType");
  var estPrice = document.getElementById("uiEstimatedPrice");

  //var url = "http://127.0.0.1:5000/predict_home_price";
  var url = "/api/predict_home_price"; 

  $.post(url, {
      newBuilding: newBuilding,
      floorNumber: floorNumber.value,
      fromDeveloper: fromDeveloper,
      isApartments: isApartments,
      isAuction: isAuction,
      kitchenArea: kitchenArea.value,
      livingArea: livingArea.value,
      roomsCount: roomsCount.value,
      totalArea: totalArea.value,
      floorsCount: floorsCount.value,
      isComplete: isComplete,
      passengerLiftsCount: passengerLiftsCount,
      cargoLiftsCount: cargoLiftsCount,
      hasBalcony: hasBalcony,
      isBasement: isBasement,
      isFirstFloor: isFirstFloor,
      isLastFloor: isLastFloor,
      flatType: flatType.value,
      region: region.value,
      city: city.value,
      materialType: materialType.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Руб</h2>";
      console.log(status);
  });
}  

  
function onPageLoad() {
  console.log( "document loaded" );
  //var url = "http://127.0.0.1:5000/get_region_names"; // Use this if you are NOT using nginx
  var url = "/api/get_region_names"; // Use this if  you are using nginx
  $.get(url,function(data, status) {
      console.log("got response for get_region_names request");
      if(data) {
          var regions = data.regions;
          var uiRegion = document.getElementById("uiRegion");
          $('#uiRegion').empty();
          for(var i in regions) {
              var opt = new Option(regions[i]);
              $('#uiRegion').append(opt);
          }
      }
  });
  //var url = "http://127.0.0.1:5000/get_city_names"; // Use this if you are NOT using nginx
  var url = "/api/get_city_names"; // Use this if  you are using nginx
  $.get(url,function(data, status) {
      console.log("got response for get_city_names request");
      if(data) {
          var cities = data.cities;
          var uiCity = document.getElementById("uiCity");
          $('#uiCity').empty();
          for(var i in cities) {
              var opt = new Option(cities[i]);
              $('#uiCity').append(opt);
          }
     }
  });
  //var url = "http://127.0.0.1:5000/get_materialtype_names"; // Use this if you are NOT using nginx
  var url = "/api/get_materialtype_names"; // Use this if  you are using nginx
  $.get(url,function(data, status) {
      console.log("got response for get_materialtype_names request");
      if(data) {
          var materialTypes = data.materialTypes;
          var uiMaterialType = document.getElementById("uiMaterialType");
          $('#uiMaterialType').empty();
          for(var i in materialTypes) {
              var opt = new Option(materialTypes[i]);
              $('#uiMaterialType').append(opt);
          }
     }
  });
  //var url = "http://127.0.0.1:5000/get_flattype_names"; // Use this if you are NOT using nginx
  var url = "/api/get_flattype_names"; // Use this if  you are using nginx
  $.get(url,function(data, status) {
      console.log("got response for get_flattype_names request");
      if(data) {
          var flatTypes = data.flatTypes;
          var uiFlatType = document.getElementById("uiFlatType");
          $('#uiFlatType').empty();
          for(var i in flatTypes) {
              var opt = new Option(flatTypes[i]);
              $('#uiFlatType').append(opt);
          }
     }
  });
}


window.onload = onPageLoad;