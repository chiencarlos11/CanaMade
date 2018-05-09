export const LAURENT_ITEMS = ['date', 'po_number', 'original_width', 'original_width_fraction', 'original_height', 'original_height_fraction',
                         'control_size', 'cassette_orientation', 'cassette_extra', 
    'cassette_color', 'fabric_type', 'fabric_color', 'cassette_size', 'tube_tob', 'inner', 'outer','height'];


export const ROLLER_SHADE_ITEMS = ['date', 'po_number', 'original_width', 'original_width_fraction', 'original_height', 'original_height_fraction',
                         'control_size', 'cassette_orientation', 'cassette_extra', 
    'cassette_color', 'fabric_type', 'fabric_color', 'cassette_size', 'tube_tob','height'];

export const CANAMADE_ITEMS = ['date', 'po_number', 'original_width', 'original_width_fraction', 'original_height', 'original_height_fraction',
                         'control_size', 'cassette_orientation', 'cassette_extra', 
    'cassette_color', 'fabric_type', 'fabric_color', 'cassette_size', 'tube_tob','height'];

export const CONTROL_SIZE = ['24','36','48','60','72','84','96'];

export const FRACTIONS = ['0','1/8','1/4','3/8','1/2','5/8','3/4','7/8'];

export const CANAMADE_ITEMS_FABRIC = {"Light Filtering": ["0101","0501","0202","1802","2501","3001"],
						"Room Darkening":["B0101","B0501","B0202","B1802","B2501","B3001"]};    



export default handleCanaMadeDataPiece(event){
    var itemMap = new Map();
    itemMap.set(event.target.name, event.target.value)
    this.handleData(itemMap)
    if (event.target.value && event.target.name === 'original_width'){
      let original_width_fraction_fraction = math.fraction(this.state.original_width_fraction)
      console.log("fraction = " + original_width_fraction_fraction)
      let new_cassette_size = (parseFloat(event.target.value) + original_width_fraction_fraction) - (3/8);
      let new_tube_tob = new_cassette_size - 1;
      return {"cassette_size":new_cassette_size,"tube_tob": new_tube_tob}
    } else if(event.target.value && event.target.name === 'original_width_fraction'){
      console.log("Setting original_width_fraction = " + event.target.value)
      let original_width = math.fraction(this.state.original_width)
      let original_width_fraction_fraction = math.fraction(this.parse_fraction(event.target.value))
      let new_cassette_size = (parseFloat(original_width) + original_width_fraction_fraction) - (3/8);
      let new_tube_tob = new_cassette_size - 1;
      return {"cassette_size":new_cassette_size,"tube_tob": new_tube_tob}
    } 

  }

