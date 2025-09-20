package com.code81.library.entity;

public enum RoleType {
    ADMINISTRATOR("ADMINISTRATOR"),
    LIBRARIAN("LIBRARIAN"),
    STAFF("STAFF");

    private final String value;

    RoleType(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return value;
    }
}