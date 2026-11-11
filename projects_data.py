# projects_data.py
# Centralized technical database for academic project showcases

PROJECTS = {
    "group-1": {
        "slug": "group-1",
        "group_name": "GROUP 1",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "AQUA CONTROL",
        "subtitle": "Automated Aquarium Water Quality Control System",
        "description": "An automated aquarium water quality management system engineered to preserve optimal biological and environmental conditions for aquatic life. The architecture coordinates multi-sensor analog/digital feedback loops to regulate water temperature, optical clarity (turbidity), and acid-base (pH) stabilization autonomously using an ESP32 microcontroller integrated with the Blynk IoT cloud platform.",
        "date": "March 1, 2025",
        "folder": "group 1",

        "members": [
            {
                "name": "Celetaria, Flint L.",
                "role": "Lead Hardware Engineer & Circuit Assembly",
                "photo": "CELETARIA.png"
            },
            {
                "name": "Manalo, Jett Axel D.",
                "role": "Firmware & IoT Cloud Architect",
                "photo": "MANALO.png"
            },
            {
                "name": "Pascua, Emma Rose L.",
                "role": "QA Systems Testing & Documentation Lead",
                "photo": "PASCUA.jfif"
            }
        ],

        "subsystems": [
            {
                "name": "1. Temperature Regulation",
                "icon": "bi-thermometer-sun",
                "color": "danger",
                "sensor": "DS18B20 Waterproof Temperature Sensor",
                "actuator": "Submersible Aquarium Heater (25W)",
                "details": "Continuously measures aquatic thermal levels. If the water temperature falls below the 28.0°C threshold, a relay triggers the heating element until thermal equilibrium is restored."
            },
            {
                "name": "2. Turbidity Filtration Control",
                "icon": "bi-water",
                "color": "info",
                "sensor": "SKU SEN0189 Optical Turbidity Sensor",
                "actuator": "DC 12V Submersible Water Pump",
                "details": "Measures water clarity via optical transmittance. When suspended particulates exceed 120 NTU, the system activates the circulation pump to drive water through the top overhead trickle filter."
            },
            {
                "name": "3. pH Buffer Stabilization",
                "icon": "bi-droplet-half",
                "color": "warning",
                "sensor": "PH-4502C Analog Liquid pH Sensor",
                "actuator": "G328 DC Peristaltic Dosing Pump",
                "details": "Monitors hydrogen-ion activity. If the reading shifts beyond acceptable boundaries (pH > 9.0), the peristaltic dosing motor meters neutralizing buffer solution to stabilize the water chemistry."
            }
        ],

        "components": [
            {
                "name": "ESP32 DevKit V1",
                "category": "Microcontroller",
                "spec": "Dual-Core Xtensa LX6 @ 240MHz | 520KB SRAM | 802.11 b/g/n Wi-Fi & BLE 4.2 | 12-bit SAR ADC",
                "desc": "Serves as the central computing unit that samples analog and digital sensor telemetry, processes automation threshold logic, actuates relay channels, and synchronizes real-time metrics with the Blynk IoT cloud dashboard.",
                "image": "esp32.jpg"
            },
            {
                "name": "DS18B20 Temperature Probe",
                "category": "Thermal Sensor",
                "spec": "Operating Range: -55°C to +125°C | Accuracy: ±0.5°C (-10°C to +85°C) | 9 to 12-bit Configurable Resolution | 1-Wire Protocol",
                "desc": "Encapsulated in a waterproof stainless steel tube, this digital sensor delivers drift-free water temperature readings over a single GPIO data line using an external 4.7kΩ pull-up resistor.",
                "image": "ds18b20.jpg"
            },
            {
                "name": "SKU SEN0189 Turbidity Sensor",
                "category": "Optical Sensor",
                "spec": "Operating Voltage: 5.0V DC | Current: 40mA (max) | Output: Analog (0-4.5V) & Digital Threshold | Response Time: <500ms | Light Wavelength: 940nm",
                "desc": "Detects total suspended solids (TSS) by calculating optical transmittance between an infrared emitter and phototransistor, mapped linearly into Nephelometric Turbidity Units (0-300 NTU).",
                "image": "turbidity.jpg"
            },
            {
                "name": "PH-4502C pH Sensor Module",
                "category": "Chemical Sensor",
                "spec": "Measurement Range: 0.00 - 14.00 pH | Accuracy: ±0.1 pH (25°C) | Response Time: ≤1 min | Supply Voltage: 5.0V DC | BNC Connector",
                "desc": "Pairs a high-impedance glass bulb electrode with an operational amplifier conditioning circuit to output a voltage signal proportional to the acidity or alkalinity of the solution.",
                "image": "ph_sensor.jpg"
            },
            {
                "name": "SRD-05VDC-SL-C Relay Module",
                "category": "Switching Actuator",
                "spec": "Control Voltage: 5V DC | Trigger Current: 5mA | Max Load: 10A 250VAC / 10A 30VDC | Optocoupler Isolation | Active LOW",
                "desc": "Provides galvanic isolation between the low-voltage ESP32 logic pins and high-current mechanical loads, switching the 220V AC heater and 12V DC pump motors safely.",
                "image": "relay.jpg"
            },
            {
                "name": "Submersible Aquarium Heater",
                "category": "Heating Actuator",
                "spec": "Power Rating: 25 Watts | Operating Voltage: 220V-240V AC | Explosion-proof Quartz Glass | Submersible IP68 Rating",
                "desc": "Supplies controlled thermal energy to the aquatic reservoir, energized via the relay module whenever water temperature drops below optimal metabolic limits.",
                "image": "heater.jpg"
            },
            {
                "name": "DC 12V Submersible Water Pump",
                "category": "Circulation Pump",
                "spec": "Rated Voltage: 12V DC | Flow Rate: 240 L/H (63 GPH) | Static Head: 3 meters | Brushless Motor | Power Consumption: 4.8W",
                "desc": "Circulates tank volume into the external multi-stage filtration compartment when elevated turbidity readings require physical mechanical filtration.",
                "image": "water_pump.jpg"
            },
            {
                "name": "G328 Peristaltic Dosing Pump",
                "category": "Metering Pump",
                "spec": "Operating Voltage: 12V DC | Flow Rate: 0 - 100 mL/min | Tubing: Food-grade Silicone (2mm ID x 4mm OD) | Self-priming",
                "desc": "Employs positive-displacement rollers to deliver precise microliter doses of pH stabilizing buffer into the aquarium without allowing fluid to touch mechanical pump gears.",
                "image": "peristaltic.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 27", "device": "Relay Channel 1 (Submersible Heater)", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 25", "device": "Relay Channel 2 (G328 Peristaltic Dosing Pump)", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 26", "device": "Relay Channel 3 (DC 12V Filtration Pump)", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 32", "device": "DS18B20 1-Wire Digital Bus", "type": "Digital Input (External Pull-up)"},
            {"pin": "GPIO 34", "device": "PH-4502C Analog Signal (Po)", "type": "Analog Input (ADC1_CH6)"},
            {"pin": "GPIO 35", "device": "SKU SEN0189 Analog Output", "type": "Analog Input (ADC1_CH7)"}
        ],

        "code_auto": """// AUTOMATIC SENSOR & ACTUATOR CONTROL LOOP
#include <OneWire.h>
#include <DallasTemperature.h>

#define RELAY_HEATER 27
#define RELAY_PUMP 25
#define RELAY_TURBIDITY 26

#define PH_SENSOR_PIN 34
#define TURBIDITY_SENSOR_PIN 35
#define TEMP_SENSOR_PIN 32

#define TEMP_THRESHOLD 28.0
#define PH_HIGH 9.0
#define PH_LOW 6.5
#define TURBIDITY_THRESHOLD 120

OneWire oneWire(TEMP_SENSOR_PIN);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  sensors.begin();
  pinMode(RELAY_HEATER, OUTPUT);
  pinMode(RELAY_PUMP, OUTPUT);
  pinMode(RELAY_TURBIDITY, OUTPUT);
  digitalWrite(RELAY_HEATER, HIGH);
  digitalWrite(RELAY_PUMP, HIGH);
  digitalWrite(RELAY_TURBIDITY, HIGH);
}

void loop() {
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  digitalWrite(RELAY_HEATER, (temperature < TEMP_THRESHOLD) ? LOW : HIGH);

  int turbidityRaw = analogRead(TURBIDITY_SENSOR_PIN);
  int ntu = map(turbidityRaw, 0, 2500, 300, 0);
  digitalWrite(RELAY_TURBIDITY, (ntu > TURBIDITY_THRESHOLD) ? LOW : HIGH);

  int phRaw = analogRead(PH_SENSOR_PIN);
  float voltage = (phRaw / 4095.0) * 3.3;
  float pH = -5.70 * voltage + (21.34 - 0.7);
  digitalWrite(RELAY_PUMP, (pH > PH_HIGH || pH < PH_LOW) ? LOW : HIGH);
  delay(2000);
}""",

        "code_blynk": """// BLYNK IOT TELEMETRY & CLOUD OVERRIDE FIRMWARE
#define BLYNK_TEMPLATE_ID "TMPL6rSCT-TIn"
#define BLYNK_TEMPLATE_NAME "SYSTEM AYOS"
#define BLYNK_AUTH_TOKEN "JBWFbF2NSONV1T12P8ZJ0MANjp7RFNCR"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>

char ssid[] = "Redmi Note 13 Pro 5G";
char pass[] = "YOUR_WIFI_PASSWORD";

BLYNK_WRITE(V8) {
  int manualPumpState = param.asInt();
  digitalWrite(RELAY_PUMP, manualPumpState ? LOW : HIGH);
}

void loop() {
  Blynk.run();
  Blynk.virtualWrite(V1, pH);
  Blynk.virtualWrite(V2, temperature);
  Blynk.virtualWrite(V3, ntu);
  Blynk.virtualWrite(V4, (temperature < TEMP_THRESHOLD) ? "Heater ON" : "Heater OFF");
}""",

        "references": [
            {"title": "Temperature Controlled Relay Switching via Thermocouple & Microcontroller", "url": "https://www.youtube.com/watch?v=GW4YsLnr02s"},
            {"title": "Design and Fabrication of DIY Multi-stage Overhead Trickle Aquarium Filters", "url": "https://www.youtube.com/watch?v=p17p1JHbETU"},
            {"title": "Industrial pH Sensor Calibration and Peristaltic Dosing Mechanics", "url": "https://www.youtube.com/watch?v=656NEt114j0"},
            {"title": "Analog pH Meter Probe Signal Conditioning and Calibration with Microcontrollers", "url": "https://www.youtube.com/watch?v=dS9-BYoazUw"}
        ],

        "media": {
            "video": "Aqua Control System.mp4",
            "pdf_presentation": "Group 1_PPT.pdf"
        }
    },

    "group-2": {
        "slug": "group-2",
        "group_name": "GROUP 2",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "AUTOMATED DUCK EGG SORTER",
        "subtitle": "Multi-Sensor Computer Vision & Candling Sorting Mechanism",
        "description": "An automated agro-industrial sorting system designed to enhance duck egg processing efficiency and eliminate manual sorting errors. Utilizing optical color inspection, high-intensity candling light transmittance, computer vision inspection via ESP32-CAM, and load cell weight classification, the machine categorizes eggs into three distinct classes: Salted Eggs (Red Eggs), Balut (fertilized embryo), and Penoy (unfertilized), guided dynamically across conveyor pathways via servo-actuated divert mechanisms.",
        "date": "March 2025",
        "folder": "group 2",

        "members": [
            {
                "name": "Pasteteo, Juliane Caye",
                "role": "System Architecture & Documentation Lead",
                "photo": "PASTETEO.jfif"
            },
            {
                "name": "Jumoc, Ernz Rabbi",
                "role": "Firmware & Optical Sensing Integrator",
                "photo": "JUMOC.jpg"
            },
            {
                "name": "Ofracio, Kevin",
                "role": "Electromechanical & Conveyor Hardware Lead",
                "photo": "OFRACIO.png"
            }
        ],

        "subsystems": [
            {
                "name": "1. Color Discrimination (Salted Red Eggs)",
                "icon": "bi-palette-fill",
                "color": "danger",
                "sensor": "TCS3200 Programmable Color Sensor",
                "actuator": "TowerPro SG90 Servo Gate 1",
                "details": "Distinguishes traditionally dyed red salted eggs from plain-shelled duck eggs using an array of color-filtered photodiodes converting reflected wavelength intensity into digital frequency."
            },
            {
                "name": "2. Embryo Candling & Vision (Balut vs. Penoy)",
                "icon": "bi-lightbulb-fill",
                "color": "warning",
                "sensor": "High-Intensity LED Candler + ESP32-CAM (OV2640) + LDR",
                "actuator": "TowerPro SG90 Servo Gate 2",
                "details": "Transilluminates the egg shell. The optical camera and light sensor inspect internal darkness: developing embryos block light transmission (classified as Balut), whereas clear fluid transmittance denotes unfertilized eggs (Penoy)."
            },
            {
                "name": "3. Continuous Conveyance & Status Display",
                "icon": "bi-arrow-repeat",
                "color": "primary",
                "sensor": "Load Cell Weight Scale + HX711 ADC",
                "actuator": "12V DC Gear Motor (Conveyor) & 0.96\" I2C OLED",
                "details": "A continuous rubber conveyor belt moves eggs along the sorting track driven by an interval-regulated 750 RPM DC motor controlled via TB6612FNG driver, while an OLED screen outputs live tally metrics."
            }
        ],

        "components": [
            {
                "name": "ESP32 WROOM-32",
                "category": "Microcontroller Unit",
                "spec": "Xtensa Dual-Core 32-bit LX6 @ 240MHz | 448KB ROM | 520KB SRAM | Integrated Wi-Fi & Dual-mode Bluetooth",
                "desc": "Acts as the central coordination controller managing sensor inputs, servo PWM divider angles, DC conveyor timing, and OLED classification output.",
                "image": "ESP32 Wroom-32.jpg"
            },
            {
                "name": "ESP32-CAM Module",
                "category": "Vision Processing",
                "spec": "OV2640 2MP Camera Sensor | Onboard Flash LED | MicroSD Slot | JPEG & BMP Image Capture",
                "desc": "Captures optical silhouettes during back-lit candling to identify internal embryonic vein formations and dark mass development separating Balut from Penoy.",
                "image": "Camera Module.jpg"
            },
            {
                "name": "TCS3200 Color Sensor",
                "category": "Optical Sensor",
                "spec": "8x8 Photodiode Matrix (Red, Green, Blue, Clear filters) | Input Voltage: 2.7V - 5.5V | High-resolution light-to-frequency conversion",
                "desc": "Measures wavelength reflectance off the eggshell surface to detect red-dyed salted duck eggs and separate them from standard natural white/green shells.",
                "image": "Color Sensor TCS3200.jpg"
            },
            {
                "name": "Candling Light Assembly",
                "category": "Optical Transilluminator",
                "spec": "High-intensity Focused LED Candler | Low-heat Radiation | High Luminescence Penetration",
                "desc": "Directs concentrated high-lumen light through the egg shell to reveal embryo presence, air cell dimensions, and yolk density without damaging organic tissue.",
                "image": "Candling Light.jpg"
            },
            {
                "name": "Light Dependent Resistor (LDR)",
                "category": "Photoelectric Sensor",
                "spec": "Spectral Peak: 540nm | Dark Resistance: 1-10 MΩ | Light Resistance: 10-20 kΩ | High sensitivity",
                "desc": "Measures differential light transmission during candling; dense embryonic masses yield higher resistance values compared to translucent unfertilized eggs.",
                "image": "Light Sensor.jpg"
            },
            {
                "name": "TB6612FNG Dual Motor Driver",
                "category": "Power Driver",
                "spec": "Operating Voltage: 4.5V - 13.5V | Constant Output Current: 1.2A per channel (3.2A peak) | MOSFET H-Bridge Architecture",
                "desc": "Drives the 12V high-torque conveyor motor efficiently with significantly lower thermal dissipation and higher efficiency than legacy L298N drivers.",
                "image": "Motor Driver.jpg"
            },
            {
                "name": "DC 12V Conveyor Motor",
                "category": "Electromechanical Actuator",
                "spec": "25mm Diameter Gearbox | 12V DC Operating Range | 750 RPM Base Speed | High Starting Torque",
                "desc": "Provides regulated rotary traction to pull the rubber conveyor belt mechanism at measured intervals along the inspection runway.",
                "image": "DC Motor.jpg"
            },
            {
                "name": "TowerPro SG90 Micro Servos",
                "category": "Positioning Actuator",
                "spec": "Operating Speed: 0.12s/60° (4.8V) | Stall Torque: 1.8 kg-cm | Operating Voltage: 4.8V - 6.0V | 180° Angular Sweep",
                "desc": "Actuates mechanical divert fins that pivot across the conveyor lane to steer categorized eggs smoothly into their respective collection trays.",
                "image": "Servo Motor.jpg"
            },
            {
                "name": "0.96\" I2C OLED Display",
                "category": "Visual Interface",
                "spec": "Resolution: 128x64 pixels | Controller: SSD1306 | Interface: I2C (SCL/SDA) | High Contrast Self-emissive Pixels",
                "desc": "Renders real-time telemetry including detected color frequencies, weight readings, classification tallies, and current conveyor throughput stats.",
                "image": "I2C OLed.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 21 (SDA)", "device": "SSD1306 OLED Display Data", "type": "I2C Serial Data"},
            {"pin": "GPIO 22 (SCL)", "device": "SSD1306 OLED Display Clock", "type": "I2C Serial Clock"},
            {"pin": "GPIO 13 / 12", "device": "TowerPro SG90 Servo Gate 1 & 2", "type": "PWM Channel 0/1 (50Hz)"},
            {"pin": "GPIO 14 / 27", "device": "TB6612FNG Motor Driver (IN1/IN2/PWM)", "type": "PWM Direction & Speed Control"},
            {"pin": "GPIO 32", "device": "Candling LDR Analog Sensor", "type": "Analog Input (ADC1_CH4)"},
            {"pin": "GPIO 4, 16, 17", "device": "TCS3200 S0, S1, S2, S3 & Out", "type": "Digital Frequency Input & Control"}
        ],

        "code_auto": """// DUCK EGG MULTI-CRITERIA SORTING & ACTUATION PIPELINE
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ESP32Servo.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

Servo servoRedEgg;
Servo servoBalutPenoy;

#define LDR_PIN 32
#define CANDLE_LIGHT_PIN 25
#define MOTOR_PWM 14
#define LDR_BALUT_THRESHOLD 1800

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  
  servoRedEgg.attach(13);
  servoBalutPenoy.attach(12);
  servoRedEgg.write(0);
  servoBalutPenoy.write(0);

  pinMode(CANDLE_LIGHT_PIN, OUTPUT);
  pinMode(LDR_PIN, INPUT);
}

void loop() {
  bool isRedEgg = checkRedColor();
  if (isRedEgg) {
    displayResult("SALTED EGG (RED)");
    servoRedEgg.write(60);
    delay(1500);
    servoRedEgg.write(0);
    return;
  }

  digitalWrite(CANDLE_LIGHT_PIN, HIGH);
  delay(300);
  int ldrValue = analogRead(LDR_PIN);
  digitalWrite(CANDLE_LIGHT_PIN, LOW);

  if (ldrValue > LDR_BALUT_THRESHOLD) {
    displayResult("BALUT (EMBRYO)");
    servoBalutPenoy.write(45);
  } else {
    displayResult("PENOY (CLEAR)");
    servoBalutPenoy.write(90);
  }
  delay(1500);
  servoBalutPenoy.write(0);
}""",

        "code_blynk": """// ESP32 CONVEYOR MOTOR TIMING & STATUS OUTPUT
#define MOTOR_IN1 26
#define MOTOR_IN2 27
#define MOTOR_PWM 14

void startConveyor(int speed) {
  digitalWrite(MOTOR_IN1, HIGH);
  digitalWrite(MOTOR_IN2, LOW);
  ledcWrite(0, speed);
}

void stopConveyor() {
  digitalWrite(MOTOR_IN1, LOW);
  digitalWrite(MOTOR_IN2, LOW);
  ledcWrite(0, 0);
}""",

        "references": [
            {
                "title": "Duck Egg Setter System with Sorting Process Using Image Processing (IEEE)",
                "url": "https://ieeexplore.ieee.org/document/10589163"
            },
            {
                "title": "An automated candling system for duck egg fertility detection, sorting, and counting via digital image processing (Magwili, 2024)",
                "url": "https://www.academia.edu/95457508"
            }
        ],

        "media": {
            "video": "DOCU.mp4",
            "pdf_presentation": "COAA PPT.pptx.pdf"
        }
    },

    "group-3": {
        "slug": "group-3",
        "group_name": "GROUP 3",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "TOMATO SORTING SYSTEM",
        "subtitle": "Automated Multi-Stage Ripeness, Defect & Size Classification Mechanism",
        "description": "An automated agricultural grading system engineered using distributed dual-microcontroller architecture (ESP32-WROOM-DA and ESP32-CAM) to evaluate tomato surface defects, ripeness, and geometric size. Tomatoes pass through an image capture inspection chamber with a 360-degree rotating servo floor, an enclosed ethylene gas sampling chamber, and optical proximity gates, autonomously routing each tomato into one of four grading bins (Small Ripe, Large Ripe, Small Unripe, Large Unripe) or an automated reject receptacle.",
        "date": "March 2025",
        "folder": "group 3",

        "members": [
            {
                "name": "Bagon, Christian",
                "role": "Computer Vision & Firmware Lead",
                "photo": "BAGON.jpg"
            },
            {
                "name": "Mandawe, Jerico",
                "role": "Mechanical Fabrication & Sensor Integration",
                "photo": "MANDAWE.png"
            },
            {
                "name": "Priol, Kevin",
                "role": "Electronics Assembly & Web Dashboard Lead",
                "photo": "PRIOL.png"
            }
        ],

        "subsystems": [
            {
                "name": "1. Vision Defect & Color Analysis",
                "icon": "bi-camera-fill",
                "color": "danger",
                "sensor": "ESP32-CAM (OV2640) + Flash LED",
                "actuator": "MG995 High-Torque Servo (Rotating Platform)",
                "details": "The tomato enters the camera chamber where an MG995 servo rotates the base platform. The ESP32-CAM captures 4 multi-angle photos to inspect surface mold or dark spots. Tomatoes with defects are immediately flagged and diverted to the reject bin."
            },
            {
                "name": "2. Ethylene Gas Ripeness Verification",
                "icon": "bi-wind",
                "color": "warning",
                "sensor": "MQ-135 Gas Sensor Module",
                "actuator": "5V DC Brushless Mini Ventilation Fan",
                "details": "In an isolated chamber sealed by servo stopper gates, the 5V mini fan draws tomato emissions across the MQ-135 gas sensor to gauge ethylene concentration, corroborating ripeness with optical color analysis."
            },
            {
                "name": "3. Height / Size Classification & Conveyance",
                "icon": "bi-rulers",
                "color": "info",
                "sensor": "TCRT5000 / VL53L0X Laser Proximity Sensor",
                "actuator": "2x 12V DC Motors (Dual Conveyor) + 4x SG90 Gates",
                "details": "The tomato traverses along twin conveyor tracks driven via an L298N motor driver. The infrared height sensor discriminates between Small and Large profiles, triggering SG90 servo flappers to divert it into its destination bin."
            }
        ],

        "components": [
            {
                "name": "ESP32 WROOM-DA",
                "category": "Main Microcontroller",
                "spec": "Dual-Core Xtensa 32-bit LX6 @ 240MHz | Dual PCB Antennas | 520KB SRAM | 30+ I/O Pins",
                "desc": "Acts as master orchestrator running the multi-state sorting state-machine, coordinating sensor acquisitions, servo gating PWM, and serving the Chart.js real-time analytics web dashboard.",
                "image": "ESP32.jpg"
            },
            {
                "name": "ESP32-CAM (AI-Thinker)",
                "category": "Computer Vision",
                "spec": "OV2640 2MP Camera Sensor | Onboard Flash LED | MicroSD Card Slot | Internal 520KB SRAM + 4MB PSRAM",
                "desc": "Executes pixel-sampling algorithms to detect dark spot defect ratios and quantify red-to-green chromatic balance across tomato facets.",
                "image": "ESP32-CAM.jpg"
            },
            {
                "name": "MQ-135 Gas Sensor",
                "category": "Chemical Gas Sensor",
                "spec": "Target Gases: NH3, NOx, Alcohol, Benzene, Smoke, CO2, Ethylene | Fast Response | Analog & Digital Output",
                "desc": "Samples ethylene gas accumulation in the testing chamber to determine natural fruit ripening stages independent of exterior pigmentation.",
                "image": "MQ-135.jpg"
            },
            {
                "name": "TCRT5000 / Range Sensor",
                "category": "Optical Distance Sensor",
                "spec": "Sensing Distance: 0.2mm - 15mm | Phototransistor & IR Diode Pair | Operating Voltage: 3.3V - 5V",
                "desc": "Detects vertical physical clearance of incoming tomatoes to classify them into Small or Large grading categories.",
                "image": "TRCRT5000.jpg"
            },
            {
                "name": "L298N Dual H-Bridge Driver",
                "category": "Motor Driver",
                "spec": "Supply Range: 5V - 35V | Peak Current: 2A per bridge | Dual H-bridge with directional inputs and PWM speed control",
                "desc": "Drives the dual DC conveyor motors with precise speed regulation and reversible forward/stop locomotion along the runway.",
                "image": "l289N MOTOR.jpg"
            },
            {
                "name": "12V DC Gear Motors",
                "category": "Drive Actuator",
                "spec": "Operating Voltage: 12V DC | High Torque Reduction Gearbox | Pull-traction rated for conveyor mechanics",
                "desc": "Powers Conveyor Belt 1 (Inspection Track) and Conveyor Belt 2 (Sorting Bin Delivery Runway).",
                "image": "12V DC MOTOR.jpg"
            },
            {
                "name": "MG995 High-Torque Servo",
                "category": "Rotary Actuator",
                "spec": "Metal Gear Train | Stall Torque: 10 kg-cm (4.8V) - 12 kg-cm (6V) | 180-degree rotation | Operating Speed: 0.20s/60°",
                "desc": "Pivots the base platform inside the camera chamber, rotating the tomato 180 degrees so the ESP32-CAM can photograph both front and back faces.",
                "image": "MG995 MOTOR.jpg"
            },
            {
                "name": "SG90 Micro Servos (x4)",
                "category": "Gate Diverter",
                "spec": "Operating Voltage: 4.8V | Stall Torque: 1.8 kg-cm | Sweep: 180 degrees | Weight: 9 grams",
                "desc": "Actuates four selective flapper gates that open and close sequentially to direct tomatoes into Bin 1, Bin 2, Bin 3, or Bin 4.",
                "image": "SG90 MOTOR.jpg"
            },
            {
                "name": "5V 4-Channel Relay Module",
                "category": "Power Switching",
                "spec": "5V Trigger Logic | Optocoupler Isolation | 10A 250VAC / 10A 30VDC rated contacts",
                "desc": "Switches independent power lines for conveyor traction motors, camera illumination, and gas chamber exhaust fans.",
                "image": "5V 4-CHANNEL.jpg"
            },
            {
                "name": "5V Mini Exhaust Fan",
                "category": "Pneumatic Airflow",
                "spec": "Dimensions: 30x30x10mm | Operating Voltage: 5V DC | Brushless Sleeve Bearing",
                "desc": "Circulates air in the ethylene testing chamber so volatile organic compounds immediately reach the MQ-135 gas sensor faceplate.",
                "image": "5V MINI FAN.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 32 / 33", "device": "Conveyor 1 & 2 PWM Speed (ENA/ENB)", "type": "PWM Channel Output (0-255)"},
            {"pin": "GPIO 27 / 14", "device": "Conveyor 2 Direction (IN3 / IN4)", "type": "Digital Output (Direction Control)"},
            {"pin": "GPIO 34", "device": "MQ-135 Gas Sensor Analog Out", "type": "Analog Input (ADC1_CH6)"},
            {"pin": "GPIO 35", "device": "TCRT5000 Height Sensor Digital Out", "type": "Digital Input (Active LOW for Large)"},
            {"pin": "GPIO 18", "device": "5V Mini Fan Control", "type": "Digital Output (Active HIGH)"},
            {"pin": "GPIO 19", "device": "Conveyor 1 Main Relay Switch", "type": "Digital Output (Relay Control)"}
        ],

        "code_auto": """// TOMATO SORTING SYSTEM - MASTER ESP32 FINITE STATE MACHINE
#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>

#define CONVEYOR1_ENA 32
#define CONVEYOR2_ENB 33
#define MQ135_PIN 34
#define TCRT5000_PIN 35
#define FAN_PIN 18
#define RELAY_CONVEYOR1 19

Servo gate1, gate2, gate3, gate4;
bool isLarge = false;
bool isRipe = false;

void setup() {
  Serial.begin(115200);
  pinMode(TCRT5000_PIN, INPUT);
  pinMode(MQ135_PIN, INPUT);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(RELAY_CONVEYOR1, OUTPUT);
  
  gate1.attach(13); gate2.attach(12); gate3.attach(14); gate4.attach(27);
  openAllSortingGates();
}

void loop() {
  isLarge = (digitalRead(TCRT5000_PIN) == LOW);
  int gasVal = analogRead(MQ135_PIN);
  isRipe = (gasVal > 2000);

  if (isRipe && !isLarge) directToBin(1);
  else if (isRipe && isLarge) directToBin(2);
  else if (!isRipe && !isLarge) directToBin(3);
  else if (!isRipe && isLarge) directToBin(4);
}

void openAllSortingGates() {
  gate1.write(90); gate2.write(90); gate3.write(90); gate4.write(90);
}

void directToBin(int binNumber) {
  openAllSortingGates();
  delay(500);
  if (binNumber == 1) gate1.write(30);
  else if (binNumber == 2) gate2.write(30);
  else if (binNumber == 3) gate3.write(30);
  else if (binNumber == 4) gate4.write(30);
}""",

        "code_blynk": """// ESP32-CAM DEFECT & COLOR RATIO PIXEL SAMPLING
#include "esp_camera.h"
#include <HTTPClient.h>

bool analyzeDarkSpots(camera_fb_t *fb) {
  if (!fb) return false;
  int darkPixelCount = 0;
  int sampleSize = 100;
  int threshold = 50;

  for (int i = 0; i < sampleSize; i++) {
    int idx = (i * fb->len / sampleSize);
    if (fb->buf[idx] < threshold) {
      darkPixelCount++;
    }
  }
  return (darkPixelCount > (sampleSize * 0.20));
}""",

        "references": [
            {
                "title": "MG995 Servo Motor Pinout Interfacing with Arduino & Microcontrollers (MicrocontrollersLab)",
                "url": "https://microcontrollerslab.com/mg995-servo-motor-pinout-interfacing-with-arduino-features-examples"
            },
            {
                "title": "How to Use MQ-135 Gas Sensor with ESP32 Using Cloud & Display (YouTube)",
                "url": "https://www.youtube.com/watch?v=CsMx5dFRM14"
            },
            {
                "title": "ESP32-CAM Video Streaming Web Server with Pan & Tilt Control (YouTube)",
                "url": "https://www.youtube.com/watch?v=hbMzerhC4ds"
            },
            {
                "title": "TCRT5000 Circuit Design & Interfacing with ESP32 (Arduino Community)",
                "url": "https://forum.arduino.cc/t/tcrt5000-circuit-for-esp32-s3/1318544"
            }
        ],

        "media": {
            "video": "Grp3-TomatoSortingSystem.mp4",
            "pdf_presentation": "Grp3-TomatoSortingSystem-PPT.pdf"
        }
    },

    "group-4": {
        "slug": "group-4",
        "group_name": "GROUP 4",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "ESP32-BASED TOMATO GREENHOUSE MONITORING SYSTEM",
        "subtitle": "Autonomous Microclimate Lighting, Ultrasonic Growth Tracking & GSM Telemetry System",
        "description": "An automated agricultural IoT solution engineered to maximize tomato cultivation productivity within a controlled greenhouse environment. The architecture combines dual-sensor acoustic and optical plant height estimation, automated morning and evening irrigation via high-torque servo sprayers, photoresistor-gated artificial UV grow light regulation for nighttime photosynthesis, and autonomous cellular SMS telemetry updates via the SIM800L module without requiring active internet connectivity.",
        "date": "March 31, 2025",
        "folder": "group 4",

        "members": [
            {
                "name": "Bernabe, Josh Christian",
                "role": "Hardware Assembly & Circuit Wiring Lead",
                "photo": "BERNABE.jpg"
            },
            {
                "name": "Marbella, Sharwin John",
                "role": "Firmware & Embedded Systems Lead",
                "photo": "MARBELLA.png"
            },
            {
                "name": "Planillo, Kim Marielle",
                "role": "System QA & Technical Documentation Lead",
                "photo": "PLANILLO.jpg"
            }
        ],

        "subsystems": [
            {
                "name": "1. Optical Plant Assessment & Sizing",
                "icon": "bi-camera-fill",
                "color": "primary",
                "sensor": "ESP32-CAM (OV2640) + HC-SR04 Ultrasonic Sensor",
                "actuator": "Internal Flash LED & Real-time Web Server",
                "details": "Monitors vertical crop development using acoustic wave time-of-flight ranging via the HC-SR04, while regular photographic snapshots from the ESP32-CAM assess fruit maturity and canopy density."
            },
            {
                "name": "2. Autonomous Scheduled Mist Irrigation",
                "icon": "bi-droplet-fill",
                "color": "info",
                "sensor": "Internal RTC / Timed Scheduling Routine",
                "actuator": "SG996R High-Torque Servo Motor (Sprayer)",
                "details": "Executes precision watering twice daily (morning and evening). The metal-gear servo pulls a pressurized mist dispenser mechanism, preventing root over-saturation and preserving soil moisture."
            },
            {
                "name": "3. Adaptive Nighttime UV Grow Lighting",
                "icon": "bi-brightness-high-fill",
                "color": "warning",
                "sensor": "Light Dependent Resistor (Photoresistor)",
                "actuator": "5V Relay Module + Full-Spectrum UV Light Bar",
                "details": "Detects ambient illuminance drops at dusk. When ambient lux falls below the preset threshold, the relay energizes artificial UV lighting to sustain chlorophyll photosynthesis through low-light cycles."
            },
            {
                "name": "4. Cellular GSM Status Reporting",
                "icon": "bi-chat-dots-fill",
                "color": "success",
                "sensor": "Growth & Fruit Diagnostic Pipeline",
                "actuator": "SIM800L GPRS / GSM Modem Module",
                "details": "Compiles plant height metrics, tomato fruit tallies, and microclimate lighting states into automated daily SMS messages sent directly to the farm operator's mobile phone without internet dependence."
            }
        ],

        "components": [
            {
                "name": "ESP32 Dev Board",
                "category": "Central Microcontroller",
                "spec": "Dual-Core Xtensa 32-bit LX6 @ 240MHz | 520KB SRAM | Integrated Wi-Fi & Bluetooth | Ultra-low Power Management",
                "desc": "Acts as the central computing unit that polls environmental analog sensors, executes timer-based irrigation logic, coordinates GSM serial communications, and drives the system's local web server.",
                "image": "ESP32.jpg"
            },
            {
                "name": "ESP32-CAM Module",
                "category": "Vision Sensor",
                "spec": "OV2640 2MP Camera Sensor | Onboard Bright Flash LED | Supports MicroSD storage | Standard JPEG compression",
                "desc": "Mounted on the greenhouse gantry to capture optical snapshots of tomato plants, enabling visual inspection of fruit presence and foliage health.",
                "image": "ESP32-CAM.jpg"
            },
            {
                "name": "HC-SR04 Ultrasonic Sensor",
                "category": "Acoustic Rangefinder",
                "spec": "Operating Voltage: 5V DC | Range: 2cm - 400cm | Accuracy: ±3mm | Measuring Angle: 15° | Trigger Input: 10µs TTL pulse",
                "desc": "Emits 40kHz ultrasound pulses toward the canopy top to measure vertical growth and canopy height without physical contact with the crop.",
                "image": "HC-SR04.jpg"
            },
            {
                "name": "Photoresistor (LDR)",
                "category": "Light Sensor",
                "spec": "Spectral Peak: 540nm | Dark Resistance: 1-10 MΩ | Light Resistance: 10-20 kΩ | High Lux Sensitivity",
                "desc": "Samples daylight availability within the enclosure, triggering supplementary artificial lighting when ambient light drops below critical photosynthetic levels.",
                "image": "PHOTORESISTOR.jpg"
            },
            {
                "name": "SIM800L GSM Module",
                "category": "Cellular Modem",
                "spec": "Quad-Band 850/900/1800/1900MHz | Micro SIM Card Slot | Serial UART Interface (AT Commands) | 3.4V - 4.4V Supply",
                "desc": "Sends automated daily cellular SMS text notifications containing tomato fruit counts, height measurements, and greenhouse status directly to the grower.",
                "image": "SIM800L.jpg"
            },
            {
                "name": "SG996R Servo Motor",
                "category": "High-Torque Actuator",
                "spec": "Metal Gear Construction | Stall Torque: 11 kg-cm (6V) | Operating Speed: 0.17s/60° | Operating Voltage: 4.8V - 7.2V",
                "desc": "Actuates the mechanical water spray trigger twice daily (morning and evening) to deliver consistent irrigation.",
                "image": "SG996R SERVO MOTOR.jpg"
            },
            {
                "name": "5V Relay Module",
                "category": "Switching Actuator",
                "spec": "Control Voltage: 5V DC | Trigger Current: 5mA | Max Load: 10A 250VAC / 10A 30VDC | Optocoupler Isolation",
                "desc": "Provides electrical isolation to switch the mains-powered UV artificial photosynthetic grow lighting safely.",
                "image": "RELAY.jpg"
            },
            {
                "name": "Artificial UV Grow Light Bar",
                "category": "Photosynthetic Lighting",
                "spec": "Full-Spectrum UV / Blue-Red Ratio | High Luminescence Output | Weather-sealed Housing",
                "desc": "Simulates natural solar wavelengths during nighttime and overcast conditions to support continuous photosynthesis in the greenhouse.",
                "image": "UV LIGHT.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 4 / 2", "device": "SIM800L GSM Module (TX / RX UART)", "type": "Serial Communication (AT Commands)"},
            {"pin": "GPIO 5", "device": "HC-SR04 Ultrasonic Trigger Pin", "type": "Digital Output (10µs High Pulse)"},
            {"pin": "GPIO 18", "device": "HC-SR04 Ultrasonic Echo Pin", "type": "Digital Input (Pulse Width Measurement)"},
            {"pin": "GPIO 34", "device": "Photoresistor (LDR) Voltage Divider", "type": "Analog Input (ADC1_CH6)"},
            {"pin": "GPIO 23", "device": "5V Relay Module (UV Grow Light Switch)", "type": "Digital Output (Active LOW / HIGH)"},
            {"pin": "GPIO 19", "device": "SG996R High-Torque Water Spray Servo", "type": "PWM Channel Output (50Hz)"}
        ],

        "code_auto": """// ESP32 TOMATO GREENHOUSE AUTOMATION & GSM FIRMWARE
#include <HardwareSerial.h>
#include <ESP32Servo.h>

#define TRIG_PIN 5
#define ECHO_PIN 18
#define LDR_PIN 34
#define RELAY_UV_PIN 23
#define SERVO_WATER_PIN 19

#define DARK_THRESHOLD 3000

Servo waterServo;
HardwareSerial sim800(1);

void setup() {
  Serial.begin(115200);
  sim800.begin(9600, SERIAL_8N1, 4, 2);
  
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LDR_PIN, INPUT);
  pinMode(RELAY_UV_PIN, OUTPUT);
  digitalWrite(RELAY_UV_PIN, HIGH);

  waterServo.attach(SERVO_WATER_PIN);
  waterServo.write(0);
}

void loop() {
  int lightVal = analogRead(LDR_PIN);
  if (lightVal > DARK_THRESHOLD) {
    digitalWrite(RELAY_UV_PIN, LOW);
  } else {
    digitalWrite(RELAY_UV_PIN, HIGH);
  }
  delay(5000);
}""",

        "code_blynk": """// ESP32 WEB SERVER DASHBOARD & REAL-TIME CONTROLS
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

void handleRoot() {
  String html = "<!DOCTYPE html><html><head><title>Greenhouse Portal</title></head><body>";
  html += "<h2>ESP32 Tomato Greenhouse Web Dashboard</h2>";
  html += "<p>Photosynthetic Light Sensor: Active</p>";
  html += "<p>Automated Irrigation Valve: Ready</p>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void setupWebServer() {
  server.on("/", handleRoot);
  server.begin();
}""",

        "references": [
            {
                "title": "How to Build an Automatic Sanitizer / Water Dispenser with Servos (YouTube)",
                "url": "https://www.youtube.com/watch?v=ZhpxzzYOIOA"
            },
            {
                "title": "SIM800L GSM SMS Interfacing Tutorial with Microcontrollers (YouTube)",
                "url": "https://www.youtube.com/watch?v=qugcj6TMlIg"
            },
            {
                "title": "Color Detection & Object Tracking using ESP32 Camera & OpenCV (HowToElectronics)",
                "url": "https://www.youtube.com/watch?v=Nm_EMeyOdkU"
            },
            {
                "title": "AC Light Bulb Control using 5V Relay Modules & Microcontrollers (Robojax)",
                "url": "https://www.youtube.com/watch?v=g6k8sPJyif8"
            }
        ],

        "media": {
            "video": "ESP32-SYSTEM-GROUP-4.mp4",
            "pdf_presentation": "GROUP-4-ESP32-BASED TOMATO GREENHOUSE MONITORING SYSTEM.pptx.pdf"
        }
    },

    "group-5": {
        "slug": "group-5",
        "group_name": "GROUP 5",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "AUTOMATED POULTRY FARM FOR ADVANCED CHICKEN FARMING",
        "subtitle": "IoT-Enabled Water Dispensing, Scheduled Feeding, RFID Tracking & Weight Telemetry System",
        "description": "An intelligent agro-industrial poultry management architecture engineered to automate essential flock sustenance and monitor individual growth trajectories. The system coordinates closed-loop liquid replenishment via an analog water level sensor and relay pump, precision food distribution timed by a hardware Real-Time Clock (RTC), contactless chick identification using RC522 RFID transponders, precision weight sampling using an HX711 24-bit ADC load cell, and dual-channel remote telemetry across an onboard ESP32 web server and a SIM800A GSM SMS alert system.",
        "date": "March 2025",
        "folder": "group 5",

        "members": [
            {
                "name": "Mallo, Edilyn",
                "role": "System Architecture & Firmware Lead",
                "photo": "MALLO.jfif"
            },
            {
                "name": "Francisco, Ramon",
                "role": "Hardware Electronics & Circuit Wiring Lead",
                "photo": "FRANCISCO.png"
            },
            {
                "name": "Talaba, Jexel",
                "role": "Mechanical Assembly & QA Testing Lead",
                "photo": "TALABA.jfif"
            }
        ],

        "subsystems": [
            {
                "name": "1. Automated Water Replenishment",
                "icon": "bi-droplet-half",
                "color": "primary",
                "sensor": "Resistive Water Level Sensor (Tank)",
                "actuator": "5V Relay Module + Submersible DC Water Pump",
                "details": "Continuously measures fluid level in the reservoir. When the water drops below the safety threshold (analog reading < 200), the relay activates the submersible pump to refill the tank, automatically shutting down upon reaching full capacity."
            },
            {
                "name": "2. Scheduled Precision Food Dispensing",
                "icon": "bi-clock-history",
                "color": "warning",
                "sensor": "HW-111 Real Time Clock (DS1302/DS3231 RTC) + NTP Server",
                "actuator": "TowerPro SG90 Micro Servo Dispenser Valve",
                "details": "Maintains strict flock nutritional timing (scheduled for 6:00, 12:00, 15:00, and 20:00). When the preset minute is reached, the servo rotates 180 degrees to open the gravity feeder hopper and closes after dispensing."
            },
            {
                "name": "3. RFID Identification & Weight Tracking",
                "icon": "bi-upc-scan",
                "color": "success",
                "sensor": "RC522 13.56MHz RFID Reader + HX711 Load Cell",
                "actuator": "Internal Non-Volatile EEPROM Tag Database",
                "details": "Chicks fitted with unique passive RFID tags trigger identification upon approaching the feeding cradle. The platform load cell records weight increments and saves historical data into 4KB EEPROM registers."
            },
            {
                "name": "4. Dual-Mode GSM SMS & Web Dashboard",
                "icon": "bi-broadcast",
                "color": "danger",
                "sensor": "Live Telemetry Aggregator (Water, Feeding, Weight)",
                "actuator": "SIM800A/L GSM Modem + ESP32 Web Server (STA/AP)",
                "details": "Operates an embedded responsive web console for live tag registration and manual overrides, while dispatching instantaneous GSM cellular SMS alerts directly to the poultry farmer if water runs out."
            }
        ],

        "components": [
            {
                "name": "ESP32 Microcontroller",
                "category": "Main Processing Unit",
                "spec": "Dual-Core Xtensa 32-bit LX6 @ 240MHz | 520KB SRAM | 4MB Flash | Dual-Mode AP/STA Wi-Fi & Bluetooth",
                "desc": "Orchestrates the entire poultry farm automation loop: polls analog water probes, manages SPI bus lines for RFID, executes HX711 sampling, and hosts the tag management web interface.",
                "image": "ESP32 Microcontroller.jpg"
            },
            {
                "name": "RC522 RFID Module",
                "category": "Contactless Identification",
                "spec": "Operating Frequency: 13.56 MHz | Communication: SPI Bus | Range: 0 - 50mm | Compatible with ISO/IEC 14443A",
                "desc": "Scans passive RFID micro-tags attached to each bird, indexing identity codes in the onboard database to track individual feeding habits and daily weight progress.",
                "image": "RC522 RFID module.jpg"
            },
            {
                "name": "HX711 Weight Sensor + Load Cell",
                "category": "Precision Weighing Sensor",
                "spec": "24-bit High-Precision Analog-to-Digital Converter | On-chip Active Low Noise PGA | 1kg - 5kg Strain Gauge Load Cell",
                "desc": "Measures chick weight during feeding visits, translating physical mechanical displacement into millivolt differential signals processed by the 24-bit converter.",
                "image": "HX711 Weight Sensor + Load Cell.jpg"
            },
            {
                "name": "HW-111 Real Time Clock (RTC)",
                "category": "Temporal Synchronizer",
                "spec": "I2C / 3-Wire Interface | Coin Battery Backup | Temperature Compensated Crystal Oscillator",
                "desc": "Keeps precise calendar and 24-hour timekeeping independent of system resets or internet connectivity to trigger automated feeding intervals accurately.",
                "image": "HW-111.jpg"
            },
            {
                "name": "Analog Water Level Sensor",
                "category": "Fluid Detection",
                "spec": "Operating Voltage: 3.3V - 5V | Sensor Area: 40x16mm | Output: Analog Resistance Mapping",
                "desc": "Submerged in the primary water tank to measure liquid levels via exposed parallel trace resistance, triggering refill alerts before depletion.",
                "image": "Water Level Sensor.jpg"
            },
            {
                "name": "Submersible Mini Water Pump",
                "category": "Fluid Actuator",
                "spec": "Operating Voltage: 3V - 6V DC | Flow Rate: 80 - 120 L/H | Lift Head: 0.3 - 0.8m | Brushless DC Motor",
                "desc": "Submerged inside the main reservoir; pumps clean water into the bird drinking troughs whenever low-water conditions are reported by the analog sensor.",
                "image": "Water Pump.jpg"
            },
            {
                "name": "TowerPro SG90 Servo Motor",
                "category": "Rotary Valve Actuator",
                "spec": "Operating Speed: 0.12s/60° (4.8V) | Stall Torque: 1.8 kg-cm | 180-degree Sweep Angle | Weight: 9g",
                "desc": "Mechanically actuates the hopper chute flap, opening to 180 degrees during feeding hours to release feed pellets and snapping closed afterward.",
                "image": "Servo Motor.jpg"
            },
            {
                "name": "SRD-05VDC-SL-C Relay Module",
                "category": "Power Switching",
                "spec": "5V DC Coil | 10A 250VAC / 10A 30VDC Contact Rating | Optocoupler Electrical Isolation",
                "desc": "Switches the water pump motor cleanly without back-EMF spikes feeding into the sensitive ESP32 GPIO logic circuitry.",
                "image": "Relay Module.jpg"
            },
            {
                "name": "SIM800A GSM / GPRS Module",
                "category": "Cellular Modem",
                "spec": "Dual-Band 900/1800MHz | Standard AT Command Set | Serial UART Interface | External High-Gain Antenna",
                "desc": "Dispatches critical cellular SMS notifications directly to the farm owner's mobile phone regarding poultry health statistics, weight anomalies, and low-water emergencies.",
                "image": "SIM800A GSM Module.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 14", "device": "TowerPro SG90 Servo Feeder Chute", "type": "PWM Channel Output (50Hz)"},
            {"pin": "GPIO 34", "device": "Analog Water Level Sensor", "type": "Analog Input (ADC1_CH6)"},
            {"pin": "GPIO 32", "device": "5V Relay Module (Water Pump Control)", "type": "Digital Output (Active HIGH)"},
            {"pin": "GPIO 21 (SS) / 22 (RST)", "device": "RC522 RFID Chip Select & Reset", "type": "SPI Bus Control Lines"},
            {"pin": "GPIO 18 / 19 / 23", "device": "RC522 SPI Bus (SCK / MISO / MOSI)", "type": "Hardware SPI Protocol"},
            {"pin": "GPIO 5 / 4", "device": "HX711 Load Cell (DOUT / SCK)", "type": "Bit-Bang Serial 24-bit Data"},
            {"pin": "GPIO 16 / 17", "device": "SIM800A GSM Serial (RX / TX)", "type": "HardwareSerial UART (9600 Baud)"}
        ],

        "code_auto": """// AUTOMATED POULTRY FARM CONTROL LOOP & SCHEDULE
#include <ESP32Servo.h>
#include <SPI.h>
#include <MFRC522.h>
#include <HX711.h>
#include <HardwareSerial.h>

#define SERVO_PIN 14
#define WATER_SENSOR_PIN 34
#define RELAY_PIN 32
#define SS_PIN 21
#define RST_PIN 22
#define HX711_DOUT 5
#define HX711_SCK 4

Servo feederServo;
MFRC522 rfid(SS_PIN, RST_PIN);
HX711 scale;
HardwareSerial sim800(1);

const int feedHours[] = {6, 12, 15, 20};
const int numFeeds = 4;

void setup() {
  Serial.begin(115200);
  SPI.begin();
  rfid.PCD_Init();
  feederServo.attach(SERVO_PIN);
  feederServo.write(0);

  pinMode(WATER_SENSOR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  scale.begin(HX711_DOUT, HX711_SCK);
  scale.set_scale(7050.0);
}

void loop() {
  int waterReading = analogRead(WATER_SENSOR_PIN);
  if (waterReading < 200) {
    digitalWrite(RELAY_PIN, HIGH);
  } else if (waterReading > 800) {
    digitalWrite(RELAY_PIN, LOW);
  }
}""",

        "code_blynk": """// EMBEDDED ESP32 WEB CONTROLLER & REST ENDPOINTS
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

void handleData() {
  int waterVal = analogRead(34);
  String json = "{\\"waterLevel\\":\\"" + String(waterVal < 200 ? "Low" : "OK") + "\\",";
  json += "\\"pumpStatus\\":" + String(digitalRead(32) ? "true" : "false") + "}";
  server.send(200, "application/json", json);
}

void setupWebServer() {
  server.on("/data", HTTP_GET, handleData);
  server.begin();
}""",

        "references": [
            {
                "title": "Automated Hen Behavior Tracking with RFID Sensor Systems (Univ. of Georgia)",
                "url": "https://www.rfidjournal.com/news/hen-behavior-tracked-with-rfid-at-university-of-georgia/202794/"
            },
            {
                "title": "Automated Feeding, Watering and Weight Identification in Poultry Science (ScienceDirect)",
                "url": "https://www.sciencedirect.com/science/article/pii/S0032579122007064"
            }
        ],

        "media": {
            "video": "group 5 vid.mp4",
            "pdf_presentation": "PPT.pdf"
        }
    },

    "group-6": {
        "slug": "group-6",
        "group_name": "GROUP 6",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "VERTICAL TOWER CULTIVATION SYSTEM",
        "subtitle": "Automated Multi-Zone Drip Irrigation, Grow Lighting & Microclimate Humidification Architecture",
        "description": "An intelligent vertical aeroponic/hydroponic tower cultivation platform engineered specifically to maximize indoor sweet basil growth density while minimizing water and electricity usage. Operating on an ESP32 microcontroller, the system continuously reads ambient lux to modulate full-spectrum LED grow lights, samples atmospheric temperature and humidity via a DHT22 sensor to trigger an ultrasonic cold-mist humidifier, and coordinates multi-tier capacitive soil moisture probes to pulse independent 5V submersible pumps for localized precision hydration.",
        "date": "March 2025",
        "folder": "group 6",

        "members": [
            {
                "name": "Tomon, Justine O.",
                "role": "Lead Hardware Assembly & Tower Fabrication",
                "photo": "TOMON.jpg"
            },
            {
                "name": "Peque, Erica M.",
                "role": "Firmware & Microclimate Automation Lead",
                "photo": "PEQUE.jpg"
            },
            {
                "name": "Garcia, Aia A.",
                "role": "Sensor Calibration & Technical Documentation Lead",
                "photo": "GARCIA, A.png"
            }
        ],

        "subsystems": [
            {
                "name": "1. Multi-Zone Drip Irrigation",
                "icon": "bi-moisture",
                "color": "primary",
                "sensor": "Capacitive Soil Moisture Sensors (v1.2 - 4 Tiers)",
                "actuator": "4x 5V Submersible DC Water Pumps via 4-Channel Relay",
                "details": "Reads moisture capacitance across 4 vertical cultivation tiers without galvanic corrosion. When a planter level dries beyond the threshold, its dedicated water pump pulses water into that tier until moisture is replenished."
            },
            {
                "name": "2. Adaptive Full-Spectrum Grow Lighting",
                "icon": "bi-brightness-high-fill",
                "color": "warning",
                "sensor": "BH1750 Ambient Digital Light Sensor (I2C)",
                "actuator": "Dual LED Grow Light Bars (Relay Channels 1 & 2)",
                "details": "Continuously measures luminous flux in lux. When ambient indoor light falls below critical photosynthetic levels (< 300 lux), the relay energizes full-spectrum LED lighting to simulate active sunlight and conserve energy when ambient light is adequate."
            },
            {
                "name": "3. Ultrasonic Microclimate Humidification",
                "icon": "bi-cloud-haze2-fill",
                "color": "info",
                "sensor": "DHT22 (AM2302) Temperature & Humidity Sensor",
                "actuator": "Ultrasonic Cold-Mist Humidifier Transducer Module",
                "details": "Basils require ambient humidity between 60% and 70%. When relative humidity drops below optimal levels, the ESP32 energizes the piezoelectric ultrasonic atomizer to produce fine mist around the vertical foliage."
            }
        ],

        "components": [
            {
                "name": "ESP-WROOM-32",
                "category": "Central Microcontroller",
                "spec": "Dual-Core Xtensa LX6 @ 240MHz | 520KB SRAM | 802.11 b/g/n Wi-Fi & BLE | Multiple ADC/I2C Buses",
                "desc": "Processes multi-channel capacitive analog inputs, communicates with I2C and 1-wire climate sensors, controls the 4-channel relay array, and serves the wireless telemetry portal.",
                "image": "ESP32.jpg"
            },
            {
                "name": "Capacitive Soil Moisture v1.2",
                "category": "Dielectric Moisture Sensor",
                "spec": "Operating Voltage: 3.3V - 5.5V | Output Voltage: 1.2V - 2.5V Analog | Corrosion-Resistant PCB Design",
                "desc": "Samples soil dielectric permittivity across the planter cups without exposing copper electrodes to electrolytic corrosion, delivering long-term analog soil moisture tracking.",
                "image": "CAPACITIVE SOIL MOISTURE.jpg"
            },
            {
                "name": "DHT22 (AM2302) Sensor",
                "category": "Environmental Sensor",
                "spec": "Humidity Range: 0-100% RH (±2% accuracy) | Temperature: -40°C to +80°C (±0.5°C) | Digital Bus",
                "desc": "Provides high-precision humidity and ambient temperature measurements to automate the vertical tower's mist humidification cycle.",
                "image": "DHT22.jpg"
            },
            {
                "name": "BH1750 Light Sensor",
                "category": "Digital Lux Sensor",
                "spec": "Measurement Range: 1 - 65535 lx | Interface: I2C Bus | Standard Spectral Response (human-eye matched)",
                "desc": "Accurately detects ambient illuminance in lux to dynamically trigger auxiliary LED grow lighting only when natural illumination is insufficient.",
                "image": "BH1750.jpg"
            },
            {
                "name": "4-Channel 5V Relay Module",
                "category": "Switching Interface",
                "spec": "Coil Voltage: 5V DC | Max Contact Rating: 10A 250VAC / 10A 30VDC | Optocoupler Galvanic Isolation",
                "desc": "Independently switches the 4 tier irrigation water pumps, grow light arrays, and the ultrasonic humidifier safely from ESP32 logic pins.",
                "image": "4 Channel Relay.jpg"
            },
            {
                "name": "5V Submersible Water Pumps",
                "category": "Pumping Actuator",
                "spec": "Operating Voltage: 3V - 5V DC | Flow Rate: 100 L/H | Lift: 0.5m | Brushless Submersible Motor",
                "desc": "Submerged in the base water bucket to push nutrient-rich water upward through flexible silicone tubing to each basil planting cup.",
                "image": "WATER PUMP.jpg"
            },
            {
                "name": "Full-Spectrum LED Grow Lights",
                "category": "Photosynthetic Lighting",
                "spec": "Dual Aluminum Bars | Red/Blue (PAR) Spectrum Ratio | High Efficiency Lumens | 12V/5V DC",
                "desc": "Provides supplemental PAR radiation tailored for basil vegetative leaf development, supporting indoor vertical growth without direct sun.",
                "image": "LED Grow Light.jpg"
            },
            {
                "name": "Ultrasonic Humidifier Module",
                "category": "Mist Generator",
                "spec": "Operating Frequency: 108kHz | Supply: 5V USB / DC | Ceramic Piezoelectric Disc Atomizer",
                "desc": "Discharges micro-droplet cold water mist directly into the vertical enclosure to elevate surrounding relative humidity during dry spells.",
                "image": "Humidifier.jpg"
            },
            {
                "name": "LM2596 DC-DC Buck Converter",
                "category": "Voltage Regulator",
                "spec": "Input: 4V - 35V DC | Output: 1.23V - 30V Adjustable | Conversion Efficiency up to 92% | Max Current: 3A",
                "desc": "Steps down high-voltage supply bricks (12V) into a stable 5V rail to power the ESP32, relays, sensors, and pumps without brownouts.",
                "image": "DC DC Converter.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 17", "device": "DHT22 Temperature & Humidity Bus", "type": "Digital 1-Wire Protocol"},
            {"pin": "GPIO 21 (SDA) / 22 (SCL)", "device": "BH1750 Ambient Light Sensor", "type": "I2C Serial Bus"},
            {"pin": "GPIO 15", "device": "Relay 1 - Ultrasonic Humidifier", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 19 / 5", "device": "Relay 2 & 3 - LED Grow Light Bars", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 25 / 26", "device": "Relay Channels - Tier 1 & 2 Water Pumps", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 4 / 14", "device": "Relay Channels - Tier 3 & 4 Water Pumps", "type": "Digital Output (Active LOW)"},
            {"pin": "GPIO 34 / 35", "device": "Capacitive Moisture Sensors (Tier 1 & 2)", "type": "Analog Input (ADC1_CH6 / CH7)"},
            {"pin": "GPIO 32 / 33", "device": "Capacitive Moisture Sensors (Tier 3 & 4)", "type": "Analog Input (ADC1_CH4 / CH5)"}
        ],

        "code_auto": """// VERTICAL TOWER CULTIVATION - COMPLETE AUTOMATION LOOP
#include <Wire.h>
#include <DHT.h>
#include <BH1750.h>

#define DHTPIN 17
#define DHTTYPE DHT22

#define RELAY_HUMIDIFIER 15
#define RELAY_LIGHT1 19
#define RELAY_LIGHT2 5
#define RELAY_PUMP1 25

#define SOIL_PIN1 34
#define DRY_SOIL_THRESHOLD 2800
#define LOW_LUX_THRESHOLD 300
#define LOW_HUMIDITY_THRESHOLD 60.0

DHT dht(DHTPIN, DHTTYPE);
BH1750 lightMeter;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  dht.begin();
  lightMeter.begin();

  pinMode(RELAY_HUMIDIFIER, OUTPUT);
  pinMode(RELAY_LIGHT1, OUTPUT);
  pinMode(RELAY_LIGHT2, OUTPUT);
  pinMode(RELAY_PUMP1, OUTPUT);

  digitalWrite(RELAY_HUMIDIFIER, HIGH);
  digitalWrite(RELAY_LIGHT1, HIGH);
  digitalWrite(RELAY_LIGHT2, HIGH);
  digitalWrite(RELAY_PUMP1, HIGH);
}

void loop() {
  float lux = lightMeter.readLightLevel();
  if (lux < LOW_LUX_THRESHOLD) {
    digitalWrite(RELAY_LIGHT1, LOW);
    digitalWrite(RELAY_LIGHT2, LOW);
  } else {
    digitalWrite(RELAY_LIGHT1, HIGH);
    digitalWrite(RELAY_LIGHT2, HIGH);
  }

  float humidity = dht.readHumidity();
  if (humidity < LOW_HUMIDITY_THRESHOLD) {
    digitalWrite(RELAY_HUMIDIFIER, LOW);
  } else {
    digitalWrite(RELAY_HUMIDIFIER, HIGH);
  }
  delay(2000);
}""",

        "code_blynk": """// ESP32 LOCAL WEB SERVER FOR VERTICAL TOWER MONITORING
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

void handleStatus() {
  String response = "{\\"status\\":\\"Tower Active\\",\\"crop\\":\\"Sweet Basil\\"}";
  server.send(200, "application/json", response);
}

void setupServer() {
  server.on("/status", HTTP_GET, handleStatus);
  server.begin();
}""",

        "references": [
            {
                "title": "Development of Vertical Indoor Farming using Arduino and IoT (Springer)",
                "url": "https://doi.org/10.1007/978-3-031-47727-0_10"
            },
            {
                "title": "Automated Vertical Farming Systems (Hackster.io)",
                "url": "https://www.hackster.io/go-b/automated-vertical-farming-72737c"
            },
            {
                "title": "Gardino: Geek Gardening with Arduino & Microcontrollers (MakeZine)",
                "url": "https://makezine.com/projects/garduino-geek-gardening/"
            },
            {
                "title": "Smart Cultivation: Arduino-based IoT Aeroponics for Indoor Farming (Academia.edu)",
                "url": "https://www.academia.edu/107406764/Smart_Cultivation_An_Arduino_based_loT_Aeroponics_System_for_Indoor_Farming"
            }
        ],

        "media": {
            "video": "0331.mp4",
            "pdf_presentation": "Vertical.pdf"
        }
    },

    "group-7": {
        "slug": "group-7",
        "group_name": "GROUP 7",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "REMOTE CONTROLLED ROBOT PLANTER",
        "subtitle": "Wireless Teleoperated 4WD Autonomous Digging, Soil Analysis & Precision Seeding Platform",
        "description": "An agile mechatronic farming rover engineered to automate the labor-intensive stages of agriculture: ground excavation, soil chemical/moisture verification, seed deposition, and localized hydration. Built upon a 4-wheel drive chassis and commanded wirelessly via dual Bluetooth/Wi-Fi serial protocols from an Android phone, the robot utilizes a high-torque DC auger drill for hole digging, capacitive soil moisture and pH probes to validate agronomic viability, an SG90 servo dispenser for metered seed release, and a relay-switched mini water pump for targeted post-planting irrigation.",
        "date": "March 2025",
        "folder": "group 7",

        "members": [
            {
                "name": "Canta, Aeron Jhon",
                "role": "Locomotion & 4WD Mechanical Chassis Lead",
                "photo": "CANTA.png"
            },
            {
                "name": "Syparrado, Paul Dominic",
                "role": "Firmware & Bluetooth Telemetry Lead",
                "photo": "SYPARRADO.PNG"
            },
            {
                "name": "Yumang, Jannella Marie Kaye",
                "role": "Agronomic Sensors & Documentation Lead",
                "photo": "YUMANG.jfif"
            }
        ],

        "subsystems": [
            {
                "name": "1. 4WD Wireless Teleoperation & Locomotion",
                "icon": "bi-controller",
                "color": "primary",
                "sensor": "Bluetooth Serial Interface (SPP Profile / Android App)",
                "actuator": "4-Wheel Chassis + L298N Dual H-Bridge Motor Driver",
                "details": "Receives directional vector commands (forward, reverse, differential turns, and PWM speed scaling) from an Android handheld device via built-in ESP32 2.4GHz Bluetooth, navigating variable garden terrain with stability."
            },
            {
                "name": "2. High-Torque Mechanical Auger Drilling",
                "icon": "bi-wrench-adjustable",
                "color": "danger",
                "sensor": "Drill Cycle Feedback Protocol",
                "actuator": "High-Torque 12V DC Motor with Spiral Auger Bit",
                "details": "Switched via power MOSFET/Relay (GPIO 23). The auger drill rotates downward into the soil bed, creating a uniform, debris-free planting hole at calibrated agronomic depths before seed release."
            },
            {
                "name": "3. In-Situ Soil Moisture & pH Diagnostics",
                "icon": "bi-moisture",
                "color": "warning",
                "sensor": "Soil Moisture Probe (GPIO 34) & Soil pH Sensor (GPIO 35)",
                "actuator": "Bespoke Android Dashboard / Serial Alert Telemetry",
                "details": "Samples dielectric moisture levels and pH acidity/alkalinity in real time. The system alerts the grower if soil conditions fall outside safe germination ranges (pH 6.5 - 7.5; moisture > 600 ADC threshold)."
            },
            {
                "name": "4. Servo Seed Metering & Targeted Irrigation",
                "icon": "bi-droplet-fill",
                "color": "info",
                "sensor": "Automated Planting State Machine",
                "actuator": "SG90 Micro Servo Seeder + 5V Relay Submersible Water Pump",
                "details": "Upon confirming favorable soil metrics, the SG90 servo pivots the seed gate to deposit seeds precisely into the excavated cavity. The relay then pulses the 5V mini water pump to irrigate the seedbed directly."
            }
        ],

        "components": [
            {
                "name": "2.4GHz ESP-32 Microcontroller",
                "category": "Central Processing Unit",
                "spec": "Dual-Core Xtensa LX6 @ 240MHz | 520KB SRAM | Integrated Bluetooth v4.2 BR/EDR & Wi-Fi | 12-bit ADC Channels",
                "desc": "Coordinates real-time Bluetooth wireless reception, executes PWM motor steering algorithms, samples analog soil diagnostic probes, and sequences the automated drilling and planting cycle.",
                "image": "esp32.jpg"
            },
            {
                "name": "4-Wheel Drive Chassis",
                "category": "Robotic Platform",
                "spec": "Laser-cut Acrylic Platform | 4x TT DC Gear Motors | High-Traction Rubber Tires | Integrated Battery Compartment",
                "desc": "Provides omnidirectional mobility across farm plots, designed with an agile low center of gravity to carry on-board seed reservoirs, water containers, and electromechanical digging modules.",
                "image": "4 wheel chassis.jpg"
            },
            {
                "name": "DC Motor Auger Driller",
                "category": "Drilling Actuator",
                "spec": "Operating Voltage: 12V DC | High-Reduction Planetary Gearbox | Heavy-Duty Helical Ground Auger Bit",
                "desc": "Provides substantial drilling torque to penetrate compacted agricultural soil, creating precise vertical holes for seed deposition without manual digging.",
                "image": "dc motor auger driller.jpg"
            },
            {
                "name": "Soil Moisture Sensor",
                "category": "Soil Diagnostic",
                "spec": "Operating Voltage: 3.3V - 5V | Dual Analog/Digital Output | Adjustable LM393 Comparator Sensitivity",
                "desc": "Measures soil volumetric water content through electrical conductivity between probe prongs, determining whether post-planting irrigation is required.",
                "image": "soil moisture sensor.jpg"
            },
            {
                "name": "Soil pH Sensor Probe",
                "category": "Chemical Diagnostic",
                "spec": "Measurement Range: 3 - 9 pH | Analog Output Interface | Standard Glass Electrode BNC Interface",
                "desc": "Assesses acidity and alkalinity levels in the soil substrate, ensuring seeds are introduced only in agronomically viable soil conditions.",
                "image": "ph soil sensor.jpg"
            },
            {
                "name": "SG90 Micro Servo",
                "category": "Dispensing Actuator",
                "spec": "Stall Torque: 1.8 kg-cm (4.8V) | Operating Speed: 0.10s/60° | 180° Angular Sweep | 9g Compact Profile",
                "desc": "Actuates the bottom hopper baffle of the seed container, opening to release a single seed into the drilled hole and quickly sealing the aperture.",
                "image": "SG90 Mirco Servo.jpg"
            },
            {
                "name": "5V Relay Module",
                "category": "Switching Interface",
                "spec": "Trigger Current: 5mA | Switching Capacity: 10A 250VAC / 10A 30VDC | Optocoupler Isolation",
                "desc": "Isolates the 3.3V ESP32 microcontroller logic while energizing the high-current DC submersible water pump for automated seed watering.",
                "image": "relay 5v.jpg"
            },
            {
                "name": "Submersible Mini Water Pump",
                "category": "Fluid Dispenser",
                "spec": "Rated Voltage: 3V - 6V DC | Flow Rate: 80 - 120 L/H | Lift: 0.3 - 0.8m | Flexible Vinyl Tube Outlet",
                "desc": "Supplies measured water pulses to freshly deposited seeds through a localized nozzle, ensuring immediate moisture for germination.",
                "image": "water pump.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 18 / 19", "device": "L298N Motor 1 Left Drive (IN1 / IN2)", "type": "Digital Direction Control"},
            {"pin": "GPIO 21 / 22", "device": "L298N Motor 2 Right Drive (IN3 / IN4)", "type": "Digital Direction Control"},
            {"pin": "GPIO 5 / 4", "device": "L298N PWM Speed Channels (ENA / ENB)", "type": "PWM Channel 0/1 (0-255 Speed)"},
            {"pin": "GPIO 23", "device": "Auger Drill DC Motor Relay / MOSFET", "type": "Digital Output (Drill ON/OFF)"},
            {"pin": "GPIO 34", "device": "Analog Soil Moisture Sensor Input", "type": "Analog Input (ADC1_CH6)"},
            {"pin": "GPIO 35", "device": "Analog Soil pH Sensor Signal", "type": "Analog Input (ADC1_CH7)"},
            {"pin": "GPIO 4 (Signal)", "device": "SG90 Micro Servo Seeder Gate", "type": "PWM Channel Output (50Hz)"},
            {"pin": "Internal", "device": "Built-in Bluetooth Serial (esp32_car)", "type": "RF Wireless SPP Profile"}
        ],

        "code_auto": """// REMOTE CONTROLLED ROBOT PLANTER - WIRELESS MOTOR & IRRIGATION PIPELINE
#include <Arduino.h>
#include "BluetoothSerial.h"
#include <ESP32Servo.h>

BluetoothSerial SerialBT;

#define EN_A 5
#define EN_B 23
#define IN1 22
#define IN2 21
#define IN3 19
#define IN4 18

#define SOIL_SENSOR_PIN 34
#define PH_SENSOR_PIN 35
#define WATER_PUMP_RELAY 4
#define SERVO_SEED_PIN 13
#define DRILL_RELAY_PIN 23

#define MOISTURE_DRY_THRESHOLD 600

Servo seedServo;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("esp32_car");
  
  pinMode(EN_A, OUTPUT); pinMode(EN_B, OUTPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  
  pinMode(WATER_PUMP_RELAY, OUTPUT);
  pinMode(DRILL_RELAY_PIN, OUTPUT);
  digitalWrite(WATER_PUMP_RELAY, LOW);
  digitalWrite(DRILL_RELAY_PIN, LOW);

  seedServo.attach(SERVO_SEED_PIN);
  seedServo.write(0);
}

void loop() {
  if (SerialBT.available()) {
    char cmd = SerialBT.read();
    executeDriveCommand(cmd);
  }

  int moisture = analogRead(SOIL_SENSOR_PIN);
  if (moisture > MOISTURE_DRY_THRESHOLD) {
    digitalWrite(WATER_PUMP_RELAY, HIGH);
    delay(2000);
    digitalWrite(WATER_PUMP_RELAY, LOW);
  }
}

void executeDriveCommand(char cmd) {
  if (cmd == 'F') {
    digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
  } else if (cmd == 'S') {
    digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);
  }
}""",

        "code_blynk": """// ESP32 ANALOG SENSOR TESTING & THRESHOLD VALIDATION
#define PH_ACIDIC 1200
#define PH_ALKALINE 1800

void testSensors() {
  int phVal = analogRead(35);
  int moistureVal = analogRead(34);

  if (phVal < PH_ACIDIC) {
    Serial.println("Soil condition: ACIDIC (pH < 6.0)");
  } else if (phVal > PH_ALKALINE) {
    Serial.println("Soil condition: ALKALINE (pH > 8.0)");
  } else {
    Serial.println("Soil condition: NEUTRAL (6.5 - 7.5 OPTIMAL)");
  }
}""",

        "references": [
            {
                "title": "Design and Development of Autonomous Agricultural Seed Sowing Robots (IEEE Xplore)",
                "url": "https://ieeexplore.ieee.org/abstract/document/9074211"
            },
            {
                "title": "Smart Farming: IoT & Bluetooth Controlled Seeding and Irrigation Rovers (ResearchGate)",
                "url": "https://www.researchgate.net/publication/342114256_IoT_Based_Smart_Agriculture_Robot"
            },
            {
                "title": "ESP32 Bluetooth Serial (Classic BT) Motor Control Architecture (RandomNerdTutorials)",
                "url": "https://randomnerdtutorials.com/esp32-bluetooth-classic-arduino-ide/"
            },
            {
                "title": "L298N Motor Driver Interfacing and DC Motor Control with ESP32 (LastMinuteEngineers)",
                "url": "https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/"
            }
        ],

        "media": {
            "video": "group 7 vid.mp4",
            "pdf_presentation": "arduino G7.pptx.pdf"
        }
    },

    "group-8": {
        "slug": "group-8",
        "group_name": "GROUP 8",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "GREENHOUSE AUTOMATION SYSTEM",
        "subtitle": "Autonomous Solar Roof Shading, Multi-Point Plant Health Color Sensing & Thermal Ventilation Architecture",
        "description": "An autonomous greenhouse automation prototype engineered to self-regulate microclimate parameters and monitor plant health metrics without manual labor. Operating through an ESP32 central computing node, the system leverages an I2C BH1750 ambient light sensor to actuate dual high-torque servo motors for opening and closing the solar roof panels based on solar radiation thresholds (300 lux), employs a TCS3200 programmable color sensor mounted on an indexing rotary platform to evaluate leaf chlorophyll health (Green vs. Brown/Yellow), and actuates a high-velocity exhaust fan via relay whenever interior temperature exceeds 30°C while the roof is closed.",
        "date": "March 2025",
        "folder": "group 8",

        "members": [
            {
                "name": "Abonita, Rovic Curtley",
                "role": "Lead Hardware Assembly & Chassis Mechanics",
                "photo": "ABONITA.png"
            },
            {
                "name": "Eledia, Kimberly",
                "role": "Firmware & Sensor Calibration Lead",
                "photo": "ELEDIA.png"
            },
            {
                "name": "Madera, Renz Mark",
                "role": "Circuit Integration & Technical Documentation Lead",
                "photo": "MADERA.png"
            }
        ],

        "subsystems": [
            {
                "name": "1. Automated Solar Roof Shading",
                "icon": "bi-sun-fill",
                "color": "warning",
                "sensor": "BH1750 Ambient Lux Sensor (I2C)",
                "actuator": "Dual MG996R / MG966R High-Torque Servos (Pins 19, 32)",
                "details": "Measures incoming solar irradiance in lux. When ambient illuminance exceeds 300 lux (excessive solar heat), the servos swing the mechanical roof closed to prevent plant scorching. During low-light conditions, the roof automatically opens to maximize natural sunlight."
            },
            {
                "name": "2. Chlorophyll Color & Health Inspection",
                "icon": "bi-flower1",
                "color": "success",
                "sensor": "TCS3200 Programmable Color Sensor Array",
                "actuator": "MG996R Rotary Plant Scanning Platform (20° Increments)",
                "details": "A rotary platform indexes pots 20 degrees per scan under the optical sensor. Leaf spectral reflectance is mapped: predominant green wavelengths signify healthy crops, while high red/yellow or brown ratios trigger unhealthy plant warnings on the monitoring console."
            },
            {
                "name": "3. Thermal Exhaust & Forced Air Ventilation",
                "icon": "bi-fan",
                "color": "info",
                "sensor": "DHT22 (AM2302) Temperature & Relative Humidity Sensor",
                "actuator": "5V Relay Module (Pin 26) + High-Speed DC Exhaust Fan",
                "details": "Protects crops from heat accumulation. If the greenhouse roof is closed and the internal chamber temperature exceeds 30.0°C, the relay triggers the exhaust fan to extract stagnant hot air until safe equilibrium is restored."
            }
        ],

        "components": [
            {
                "name": "ESP32 Dev Board",
                "category": "Central Microcontroller",
                "spec": "Dual-Core Xtensa 32-bit LX6 @ 240MHz | 520KB SRAM | 802.11 b/g/n Wi-Fi & BLE | Integrated I2C/PWM Timers",
                "desc": "Acts as the central automation brain reading sensor telemetry, sequencing roof and rotary platform servo positions, controlling the exhaust relay, and serving real-time greenhouse metrics.",
                "image": "esp32.jpg"
            },
            {
                "name": "TCS3200 Color Sensor",
                "category": "Optical Health Sensor",
                "spec": "8x8 Photodiode Matrix (Red, Green, Blue, Clear) | Light-to-Frequency Conversion | 4 Integrated White LEDs",
                "desc": "Samples reflected RGB wavelengths from plant foliage to classify crop vitality into Healthy (Green) or Unhealthy (Brown/Yellow) categories.",
                "image": "TCS3200- COLOR SENSOR.jpg"
            },
            {
                "name": "DHT22 Temperature & Humidity Sensor",
                "category": "Microclimate Sensor",
                "spec": "Temperature: -40°C to +80°C (±0.5°C) | Humidity: 0-100% RH (±2%) | Digital Signal Output",
                "desc": "Monitors internal ambient heat and atmospheric moisture, providing thermal telemetry that governs the automated ventilation exhaust fan.",
                "image": "DHT22 - TEMPERATURE & HUMIDITY SENSOR.jpg"
            },
            {
                "name": "BH1750 Ambient Light Sensor",
                "category": "Digital Lux Sensor",
                "spec": "Measurement Range: 1 - 65535 lx | Communication: I2C Interface | Built-in 16-bit ADC",
                "desc": "Measures daylight intensity inside the greenhouse, comparing real-time lux readings against the 300 lux threshold to trigger automated roof movement.",
                "image": "BH1750- LIGHT SENSOR.jpg"
            },
            {
                "name": "MG996R / MG966R Servo Motors",
                "category": "High-Torque Actuators",
                "spec": "Metal Gear Construction | Stall Torque: 11 kg-cm (6V) | Operating Speed: 0.17s/60° | 180° Sweep",
                "desc": "Employed in a dual-drive configuration to articulate the heavy greenhouse roof panels open and closed, and as a rotary actuator under the plant platform.",
                "image": "MG966R.jpg"
            },
            {
                "name": "High-Velocity Exhaust Fan",
                "category": "Ventilation Actuator",
                "spec": "Supply Voltage: 5V - 12V DC | Brushless Sleeve Bearing | High CFM Airflow Rate",
                "desc": "Mounted on the greenhouse gable wall to expel hot air and pull in fresh air whenever ambient temperatures rise above 30°C.",
                "image": "exhaust fan.jpg"
            },
            {
                "name": "Single-Channel 5V Relay Module",
                "category": "Switching Interface",
                "spec": "5V DC Coil Trigger | Optocoupler Isolation | Switching Capacity: 10A 250VAC / 10A 30VDC",
                "desc": "Provides electrical isolation between the sensitive ESP32 logic output on GPIO 26 and the power line feeding the exhaust ventilation fan.",
                "image": "RELAY MODULE.jpg"
            },
            {
                "name": "Battery Pack Holder",
                "category": "Power Distribution",
                "spec": "Multi-Cell AA / 18650 Battery Compartment | Dual Terminal Leads | Heavy-Duty Spring Terminals",
                "desc": "Supplies portable DC electrical power to the servo rail and exhaust fan, decoupling high-current actuator draws from the microcontroller logic rail.",
                "image": "BATTERY HOLDER.jpg"
            },
            {
                "name": "Interconnect DuPont Jumper Wires",
                "category": "Wiring Infrastructure",
                "spec": "Male-to-Male / Male-to-Female Multicore Copper Conductors | Standard 2.54mm Pitch Pin Headers",
                "desc": "Facilitates clean signal bus routing across the breadboard between sensor inputs, servo control leads, relay triggers, and power rails.",
                "image": "WIRES.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 21 (SDA) / 22 (SCL)", "device": "BH1750 Ambient Lux Sensor", "type": "I2C Serial Communication Bus"},
            {"pin": "GPIO 17", "device": "DHT22 Digital Temperature & Humidity Data", "type": "Single-Wire Digital Protocol"},
            {"pin": "GPIO 19 / 32", "device": "Dual MG996R Roof Actuation Servos", "type": "PWM Servo Channels (50Hz)"},
            {"pin": "GPIO 26", "device": "5V Relay Module (Exhaust Fan Control)", "type": "Digital Output (Active HIGH)"},
            {"pin": "GPIO 14", "device": "MG996R Plant Platform Rotary Servo", "type": "PWM Servo Channel (20° Indexing)"},
            {"pin": "GPIO 4, 16, 18, 5", "device": "TCS3200 S0, S1, S2, S3 Filters & Out", "type": "Frequency Output & Color Selection"}
        ],

        "code_auto": """// GREENHOUSE AUTOMATION SYSTEM - DUAL SENSOR & ACTUATION PIPELINE
#include <Wire.h>
#include <DHT.h>
#include <BH1750.h>
#include <ESP32Servo.h>

#define DHTPIN 17
#define DHTTYPE DHT22

#define ROOF_SERVO1_PIN 19
#define ROOF_SERVO2_PIN 32
#define PLATFORM_SERVO_PIN 14
#define FAN_RELAY_PIN 26

#define LIGHT_THRESHOLD 300
#define TEMP_THRESHOLD 30.0

DHT dht(DHTPIN, DHTTYPE);
BH1750 lightMeter;
Servo roofServo1, roofServo2, platformServo;

bool roofClosed = false;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  dht.begin();
  lightMeter.begin();

  roofServo1.attach(ROOF_SERVO1_PIN);
  roofServo2.attach(ROOF_SERVO2_PIN);
  platformServo.attach(PLATFORM_SERVO_PIN);

  pinMode(FAN_RELAY_PIN, OUTPUT);
  digitalWrite(FAN_RELAY_PIN, LOW);

  setRoofPosition(0);
}

void loop() {
  float lux = lightMeter.readLightLevel();
  if (lux > LIGHT_THRESHOLD) {
    setRoofPosition(90);
    roofClosed = true;
  } else {
    setRoofPosition(0);
    roofClosed = false;
  }

  float temperature = dht.readTemperature();
  if (roofClosed && temperature > TEMP_THRESHOLD) {
    digitalWrite(FAN_RELAY_PIN, HIGH);
  } else {
    digitalWrite(FAN_RELAY_PIN, LOW);
  }

  rotatePlantPlatform();
  delay(3000);
}

void setRoofPosition(int angle) {
  roofServo1.write(angle);
  roofServo2.write(180 - angle);
}

void rotatePlantPlatform() {
  static int angle = 0;
  angle = (angle == 0) ? 20 : 0;
  platformServo.write(angle);
}""",

        "code_blynk": """// ESP32 REAL-TIME GREENHOUSE MONITORING PORTAL
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

void handleTelemetry() {
  String response = "{\\"roofStatus\\":\\"" + String(roofClosed ? "Closed (Shaded)" : "Open (Daylight)") + "\\",";
  response += "\\"fanState\\":\\"" + String(digitalRead(26) ? "Active" : "Idle") + "\\"}";
  server.send(200, "application/json", response);
}

void setupServer() {
  server.on("/telemetry", HTTP_GET, handleTelemetry);
  server.begin();
}""",

        "references": [
            {
                "title": "Smart Greenhouse Climate Control using IoT and Sensors (IEEE)",
                "url": "https://ieeexplore.ieee.org/document/9397148"
            },
            {
                "title": "Automated Solar Shading and Ventilation for Indoor Crop Yield (ResearchGate)",
                "url": "https://www.researchgate.net/publication/348921102_Smart_Greenhouse_Automation"
            },
            {
                "title": "TCS3200 Color Sensor Interfacing with ESP32 (RandomNerdTutorials)",
                "url": "https://randomnerdtutorials.com/esp32-tcs3200-color-sensor/"
            },
            {
                "title": "BH1750 Ambient Light Sensor Calibration with Arduino & ESP32 (LastMinuteEngineers)",
                "url": "https://lastminuteengineers.com/bh1750-ambient-light-sensor-arduino-tutorial/"
            }
        ],

        "media": {
            "video": "group 8 vid.mp4",
            "pdf_presentation": "group 8.pdf"
        }
    },

    "group-9": {
        "slug": "group-9",
        "group_name": "GROUP 9",
        "topic": "Microprocessor Systems & Computer Organization",
        "title": "NUTRIENT AND SOIL HEALTH MONITORING FOR MUSTARD GREENS",
        "subtitle": "Precision Gravimetric Fertilizer Dosing, Slurry Agitation & Hydro-Soil Monitoring Architecture",
        "description": "An autonomous nutrient management and precision irrigation platform engineered to optimize the cultivation of mustard greens while preventing fertilizer runoff and soil salinization. Controlled by an ESP32 WROOM microcontroller, the system measures liquid fertilizer payload delivery using an HX711 24-bit ADC load cell scale, continuously agitates nutrient solutions via a worm gear motor, polls dielectric soil moisture and chemical pH to evaluate root-zone health, and drives a high-pressure 5V relay pump delivering fertilizer through an 8-hole spray manifold.",
        "date": "March 2025",
        "folder": "group 9",

        "members": [
            {
                "name": "Ajusan, Ronald O.",
                "role": "Lead Hardware Assembly & Mechanical Fabrication",
                "photo": "AJUSAN.PNG"
            },
            {
                "name": "Famini, Cristel Kate M.",
                "role": "QA Systems Testing & Documentation Lead",
                "photo": "FAMINI.png"
            },
            {
                "name": "Rosario, Jerome Steven S.",
                "role": "Firmware & Sensor Calibration Lead",
                "photo": "ROSARIO.jpg"
            }
        ],

        "subsystems": [
            {
                "name": "1. Gravimetric Precision Nutrient Dosing",
                "icon": "bi-speedometer2",
                "color": "danger",
                "sensor": "HX711 24-bit ADC + Strain Gauge Load Cell",
                "actuator": "Automated Mixing Bowl Valve / Metering Chute",
                "details": "Weighs the exact mass of fertilizer compounds before liquid introduction. Ensures optimal agronomic dosage rates for mustard greens, preventing chemical toxicity and root burning caused by over-fertilization."
            },
            {
                "name": "2. High-Torque Nutrient Slurry Agitation",
                "icon": "bi-arrow-clockwise",
                "color": "warning",
                "sensor": "Motor Driver PWM Timing Cycle",
                "actuator": "High-Torque DC Worm Gear Motor",
                "details": "Drives mechanical mixing paddles in the solution bowl. The self-locking worm gearbox provides strong rotary torque to dissolve dense fertilizer powders uniformly into irrigation water before pumping."
            },
            {
                "name": "3. Soil Dielectric Moisture & pH Diagnostics",
                "icon": "bi-moisture",
                "color": "info",
                "sensor": "Capacitive Soil Moisture Probe & Soil pH Probe",
                "actuator": "Closed-Loop Irrigation Automation State Machine",
                "details": "Monitors subterranean moisture levels to verify if fertilization should be combined with pure water hydration, while the pH probe ensures soil acidity remains within optimal uptake ranges (pH 6.0 - 7.0)."
            },
            {
                "name": "4. Pressurized 8-Hole Manifold Irrigation",
                "icon": "bi-droplet-fill",
                "color": "success",
                "sensor": "Soil Moisture Threshold Trigger",
                "actuator": "5V Submersible Water Pump via Relay + 8-Hole Spray Nozzle",
                "details": "Channels mixed fertilizer solution from the reservoir tank through vinyl hoses to an 8-hole spray nozzle, ensuring gentle, uniform radial dispersion across foliage and root beds."
            }
        ],

        "components": [
            {
                "name": "ESP32 WROOM Microcontroller",
                "category": "Central Processing Unit",
                "spec": "Dual-Core Xtensa LX6 @ 240MHz | 520KB SRAM | Integrated 802.11 b/g/n Wi-Fi & BLE | 12-bit ADC SAR",
                "desc": "Acts as the central automation brain reading load cell weights, sampling capacitive moisture and pH probes, sequencing the worm gear motor, and triggering irrigation pumps.",
                "image": "ESP32.jpg"
            },
            {
                "name": "Weight Sensor (HX711) + Load Cell",
                "category": "Gravimetric Sensor",
                "spec": "24-bit High-Precision ADC | Differential Input PGA | 1kg - 5kg Aluminum Strain Gauge Bar",
                "desc": "Quantifies dry and liquid fertilizer weight down to gram precision, ensuring exact nutritional concentrations according to plant growth stage.",
                "image": "Weight Sensor (HX711) + load cell.jpg"
            },
            {
                "name": "Capacitive Soil Moisture Sensor",
                "category": "Dielectric Sensor",
                "spec": "Operating Voltage: 3.3V - 5.5V | Analog Output (1.2V - 2.5V) | Corrosion-Resistant PCB Substrate",
                "desc": "Measures soil dielectric capacitance without exposing electrodes to soil moisture electrolysis, providing stable analog moisture metrics.",
                "image": "Soil Moisture Sensor.jpg"
            },
            {
                "name": "Soil pH Sensor Module",
                "category": "Chemical Diagnostic",
                "spec": "Measurement Range: 3.0 - 9.0 pH | Standard BNC Glass Electrode | Signal Conditioning Board",
                "desc": "Detects soil acidity and alkalinity to ensure fertilizer delivery does not acidify the soil bed beyond mustard green absorption limits.",
                "image": "pH Sensor.jpg"
            },
            {
                "name": "DC Worm Gear Motor + Driver",
                "category": "Mixing Actuator",
                "spec": "Operating Voltage: 12V DC | High-Reduction Self-Locking Worm Gearbox | High Starting Torque",
                "desc": "Rotates the internal paddle mechanism in the fertilizer reservoir to achieve homogeneous liquid-nutrient mixing before spray discharge.",
                "image": "Gear Worm Motor - Motor.jpg"
            },
            {
                "name": "Submersible Water Pump + Relay",
                "category": "Fluid Delivery",
                "spec": "Submersible DC Motor | 5V Optocoupled Relay Switch | 120 L/H Flow Capacity | 10A 250VAC Relay Contacts",
                "desc": "Pumps nutrient solution from the storage tank into the distribution manifold when soil moisture analysis detects irrigation necessity.",
                "image": "Water Pump + Relay.jpg"
            },
            {
                "name": "8-Hole Radial Spray Nozzle",
                "category": "Dispersion Head",
                "spec": "8-Point Radial Mist Outlet | Chemical-Resistant Polymer Construction | Low-Pressure Operation",
                "desc": "Atomizes fertilizer liquid into gentle droplet streams, dispersing nutrients evenly across plant beds without eroding topsoil.",
                "image": "8-hole Nozzle.jpg"
            },
            {
                "name": "Nutrient Solution Reservoir Tank",
                "category": "Fluid Storage",
                "spec": "High-Density Polyethylene (HDPE) | Translucent Volume Markings | Corrosion-Proof",
                "desc": "Holds the pre-mixed liquid reserve used for scheduled irrigation and automated nutrient delivery cycles.",
                "image": "Tank.jpg"
            },
            {
                "name": "Irrigation Delivery Vinyl Hose",
                "category": "Fluid Conduit",
                "spec": "Flexible Food-Grade PVC Tubing | 8mm Outer Diameter | Kink-Resistant Wall Thickness",
                "desc": "Channels pumped nutrient water from the storage reservoir directly to the 8-hole spray manifold.",
                "image": "Hose.jpg"
            },
            {
                "name": "Fertilizer Mixing Bowl & Cradle",
                "category": "Agitation Vessel",
                "spec": "Chemical-Resistant Polypropylene | Calibrated Volumetric Capacity | Integrated Agitator Port",
                "desc": "Serves as the dissolution vessel where raw fertilizer components are weighed, mixed with water, and prepared for crop distribution.",
                "image": "bowl.jpg"
            }
        ],

        "hardware_pins": [
            {"pin": "GPIO 5 (DOUT) / 4 (SCK)", "device": "HX711 Load Cell ADC Interface", "type": "Bit-Bang Serial Protocol"},
            {"pin": "GPIO 34", "device": "Capacitive Soil Moisture Analog Out", "type": "Analog Input (ADC1_CH6)"},
            {"pin": "GPIO 35", "device": "Soil pH Sensor Signal Conditioning Board", "type": "Analog Input (ADC1_CH7)"},
            {"pin": "GPIO 19 / 21", "device": "Worm Gear Agitator Motor Driver", "type": "PWM Direction & Speed Control"},
            {"pin": "GPIO 23", "device": "5V Relay Module (Submersible Pump Switch)", "type": "Digital Output (Active LOW)"}
        ],

        "code_auto": """// MUSTARD GREENS NUTRIENT & IRRIGATION MASTER CONTROLLER
#include <HX711.h>

#define HX711_DOUT 5
#define HX711_SCK 4
#define SOIL_MOISTURE_PIN 34
#define SOIL_PH_PIN 35
#define PUMP_RELAY_PIN 23
#define MOTOR_MIX_PIN 19

#define MOISTURE_DRY_THRESHOLD 2600
#define TARGET_FERTILIZER_WEIGHT 50.0 // Grams

HX711 scale;

void setup() {
  Serial.begin(115200);
  pinMode(PUMP_RELAY_PIN, OUTPUT);
  pinMode(MOTOR_MIX_PIN, OUTPUT);
  pinMode(SOIL_MOISTURE_PIN, INPUT);
  pinMode(SOIL_PH_PIN, INPUT);

  digitalWrite(PUMP_RELAY_PIN, HIGH); // Relay OFF
  digitalWrite(MOTOR_MIX_PIN, LOW);   // Motor OFF

  scale.begin(HX711_DOUT, HX711_SCK);
  scale.set_scale(420.0); // Calibration factor
  scale.tare();
}

void loop() {
  // 1. Measure Soil Health
  int moistureRaw = analogRead(SOIL_MOISTURE_PIN);
  int phRaw = analogRead(SOIL_PH_PIN);

  // 2. Gravimetric Nutrients & Automated Agitation
  float currentNutrientWeight = scale.get_units(5);
  if (currentNutrientWeight >= TARGET_FERTILIZER_WEIGHT) {
    // Run worm gear agitator to blend fertilizer
    digitalWrite(MOTOR_MIX_PIN, HIGH);
    delay(5000);
    digitalWrite(MOTOR_MIX_PIN, LOW);
  }

  // 3. Automated Root Hydration
  if (moistureRaw > MOISTURE_DRY_THRESHOLD) {
    digitalWrite(PUMP_RELAY_PIN, LOW); // Pump ON
    delay(4000);
    digitalWrite(PUMP_RELAY_PIN, HIGH); // Pump OFF
  }

  delay(3000);
}""",

        "code_blynk": """// ESP32 LOCAL WEB TELEMETRY & IRRIGATION OVERRIDE
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

void handleSoilStatus() {
  String response = "{\\"crop\\":\\"Mustard Greens\\",\\"status\\":\\"Soil Monitored\\"}";
  server.send(200, "application/json", response);
}

void setupServer() {
  server.on("/status", HTTP_GET, handleSoilStatus);
  server.begin();
}""",

        "references": [
            {
                "title": "Manufacture of Organic Compost Using Arduino Technology (Journal of Young Physicists)",
                "url": "https://www.journalofyoungphysicists.org/post/manufacture-of-organic-compost-using-technology"
            },
            {
                "title": "Design of Automatic Organic Waste Crusher using Arduino Microcontrollers (JEEMECS)",
                "url": "https://jurnal.unmer.ac.id/index.php/jeemecs/article/view/2377"
            },
            {
                "title": "Automated Plant Watering & Precision Irrigation Systems (YouTube)",
                "url": "https://youtu.be/ojhrVsBs0nM"
            }
        ],

        "media": {
            "video": "IMG_6142.MOV",
            "pdf_presentation": "ESP32_BASED-NUTRIENT AND SOIL MONITORING SYSTEM FOR MUSTARD GREENS.pdf"
        }
    }
}