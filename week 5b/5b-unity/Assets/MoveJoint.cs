using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveJoint : MonoBehaviour {
	public string keyForward;
    public string keyNeutral;
    public string keyBack;

    // Use this for initialization
    void Start () {
		if (keyForward == null || keyBack == null || keyNeutral == null) {
			throw new NotImplementedException("key is null");
		}	
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKey(keyForward)) {
		    Debug.Log("called");
		    HingeJoint hinge = GetComponent<HingeJoint>();
		    JointMotor motor = hinge.motor;
		    motor.force = 100;
		    motor.targetVelocity = 90;
		    motor.freeSpin = false;
		    hinge.motor = motor;
		    hinge.useMotor = true;
            
        }
	    if (Input.GetKey(keyNeutral))
	    {
	        Debug.Log("called");
	        HingeJoint hinge = GetComponent<HingeJoint>();
	        JointMotor motor = hinge.motor;
	        motor.force = 0;
	        motor.targetVelocity = 0;
	        motor.freeSpin = false;
	        hinge.motor = motor;
	        hinge.useMotor = true;
	    }
        if (Input.GetKey(keyBack))
	    {
	        Debug.Log("called");
	        HingeJoint hinge = GetComponent<HingeJoint>();
	        JointMotor motor = hinge.motor;
	        motor.force = 100;
	        motor.targetVelocity = -200;
	        motor.freeSpin = false;
	        hinge.motor = motor;
	        hinge.useMotor = true;
	    }
    }
}
