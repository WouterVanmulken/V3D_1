using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimalWalkScript : MonoBehaviour
{
    public string keyForward;
    public string keyBackwards;
    

    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
	    if (Input.GetKey(keyForward))
	    {
	        Debug.Log("called");
	        HingeJoint hinge = GetComponent<HingeJoint>();
	        JointMotor motor = hinge.motor;
	        motor.force = 100;
	        motor.targetVelocity = 90;
	        motor.freeSpin = false;
	        hinge.motor = motor;
	        hinge.useMotor = true;

	    }
	    if (Input.GetKey(keyBackwards))
	    {
	        Debug.Log("called");
	        HingeJoint hinge = GetComponent<HingeJoint>();
	        JointMotor motor = hinge.motor;
	        motor.force = -100;
	        motor.targetVelocity = -90;
	        motor.freeSpin = false;
	        hinge.motor = motor;
	        hinge.useMotor = true;

	    }
    }
}
