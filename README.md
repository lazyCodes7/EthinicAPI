
<p align="center">


  <h3 align="center">Ethinic-API</h3>

  <p align="center">
    EthinicAPI is a RESTful API which is written in Python and predicts the ethinicity, age and gender from an image provided by the user.

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


I was working on an Android-app that promoted equality and I wanted to use the pytorch model that I had but there were a lot of issues and very less support. This was the reason I built this API. Ethinic-API was built so that I could predict the race, age and gender of a person in my Android-app. A funny story I guess.


### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [OpenCV](https://opencv.org/)
* [PyTorch](https://pytorch.org/)



<!-- GETTING STARTED -->
## Getting Started

Follow the instructions to setup the project locally!

### Prerequisites

Make sure to have virtualenv package from python installed before proceeding to installation.
  ```sh
  pip install virtualenv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lazyCodes7/EthinicAPI.git
   ```
2. Activate the virtual environment
   ```sh
   cd EthinicAPI
   virtualenv venv
   . venv/bin/activate
   ```
3. Install the required packages using pip
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app
   ```sh
   python app.py
   ```
4. Start using the API at '/predict' endpoint in Postman
   ![Screenshot from 2021-07-15 18-33-42](https://user-images.githubusercontent.com/53506835/125792759-ecff30ca-ba09-43a4-804b-111954a3b2d6.png)



<!-- USAGE EXAMPLES -->
## Usage
1. Use on postman
The API can be accessed at the following [endpoint](https://ethinic-api.herokuapp.com/predict) on Postman by making a POST request in the following way.
![ezgif com-gif-maker](https://user-images.githubusercontent.com/53506835/125794643-8768c100-3047-4d52-b9d8-d65c882f04a6.gif)

2. Use the RaceClassifier inside the 'classifier' directory to make predictions
```python
# image = cv2.imread(cvImage) (uncomment this line in RaceClassifier.py)
# then import it
from classifier.RaceClassifier import *
clf = RaceClassifer(model_path="fair_face_models/res34_fair_align_multi_7_20190809.pt")
clf.predict(image_path="path to your desired image")
```
## Output
![georgina](https://user-images.githubusercontent.com/53506835/125807475-e8c237a8-dff9-4e13-ac9f-fbddeab5626c.jpg)
![output-img!](https://user-images.githubusercontent.com/53506835/125807236-319d9207-8ae5-47df-978d-d44a1379ccaa.png)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/lazyCodes7/EthinicAPI/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Rishab Mudliar - [@cheesetaco19](https://twitter.com/cheesetaco19) - rishabmudliar@gmail.com

Telegram: [lazyCodes7](https://t.me/lazyCodes7)
